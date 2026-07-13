// AQS Scorer Web Dashboard Frontend Application Logic

// Global state variables
let authorsData = [];
let selectedAuthor = null;
let radarChart = null;

// Dimension weights map
const DIMENSIONS_MAP = {
  "D1": { name: "Thought Leadership Status", weight: 41.4 },
  "D2": { name: "Tech Demand", weight: 33.0 },
  "D3": { name: "Alignment", weight: 27.6 },
  "D4": { name: "Experience", weight: 27.6 },
  "D5": { name: "Expertise", weight: 27.6 },
  "D6": { name: "Recognition", weight: 21.9 },
  "D7": { name: "Innovation", weight: 24.0 },
  "D8": { name: "Publications", weight: 11.1 },
  "D9": { name: "Reach", weight: 54.9 },
  "D10": { name: "Writing Quality", weight: 16.5 },
  "D11": { name: "Academic Credentials", weight: 11.1 },
  "D12": { name: "Cross-disciplinary Reach", weight: 3.3 }
};

// AQS Range classifier
function getAqsRange(score) {
  if (score >= 260) return { label: "Canonical Thought Leader", class: "range-canonical" };
  if (score >= 230) return { label: "Emerging Thought Leader", class: "range-emerging" };
  if (score >= 190) return { label: "IT Rockstar", class: "range-rockstar" };
  if (score >= 160) return { label: "Industry Expert", class: "range-expert" };
  if (score >= 130) return { label: "Topic Specialist", class: "range-specialist" };
  return { label: "Tech Pro", class: "range-pro" };
}

// App Initialization
document.addEventListener("DOMContentLoaded", () => {
  loadDashboardData();
  
  // Set up search and filter listeners
  document.getElementById("search-input").addEventListener("input", filterAuthors);
  document.getElementById("range-filter").addEventListener("change", filterAuthors);
});

// Load results file
async function loadDashboardData() {
  const authorListContainer = document.getElementById("author-list");
  
  try {
    const response = await fetch("aqs_test_results.json");
    if (!response.ok) {
      throw new Error("Result JSON file not found.");
    }
    
    const rawData = await response.json();
    // Filter only successfully processed records
    authorsData = rawData.filter(item => item.success);
    
    if (authorsData.length === 0) {
      authorListContainer.innerHTML = `
        <div class="loading-state">
          <i class="fa-solid fa-triangle-exclamation"></i>
          <p>No scored authors found in results file. Run the python scorer first.</p>
        </div>
      `;
      return;
    }
    
    // Calculate global stats
    calculateStats();
    renderCohortDistribution();
    
    // Populate list of authors
    renderAuthorList(authorsData);
    
  } catch (error) {
    console.error("Error loading dashboard data:", error);
    authorListContainer.innerHTML = `
      <div class="loading-state">
        <i class="fa-solid fa-triangle-exclamation" style="color: var(--color-danger)"></i>
        <p>Could not load aqs_test_results.json.<br>Verify the python script has finished running.</p>
      </div>
    `;
  }
}

// Stats Calculation
function calculateStats() {
  const total = authorsData.length;
  document.getElementById("stat-total").innerText = total;
  
  let totalExisting = 0;
  let totalComputed = 0;
  let totalAbsDiff = 0;
  
  authorsData.forEach(author => {
    totalExisting += author.existing_aqs;
    totalComputed += author.computed_aqs;
    totalAbsDiff += Math.abs(author.difference);
  });
  
  const avgExisting = totalExisting / total;
  const avgComputed = totalComputed / total;
  const mae = totalAbsDiff / total;
  
  document.getElementById("stat-avg-existing").innerText = avgExisting.toFixed(1);
  document.getElementById("stat-avg-computed").innerText = avgComputed.toFixed(1);
  document.getElementById("stat-mae").innerText = mae.toFixed(1);
  
  // Highlight MAE card based on performance
  const maeCard = document.getElementById("mae-card");
  if (mae <= 15) {
    maeCard.className = "summary-card text-glow-green";
  } else if (mae <= 30) {
    maeCard.className = "summary-card";
    maeCard.style.borderColor = "rgba(245, 158, 11, 0.25)";
    maeCard.style.boxShadow = "0 0 15px rgba(245, 158, 11, 0.1)";
  } else {
    maeCard.className = "summary-card";
    maeCard.style.borderColor = "rgba(239, 68, 68, 0.25)";
    maeCard.style.boxShadow = "0 0 15px rgba(239, 68, 68, 0.1)";
  }
}

// Render Cohort Distribution and Shift
function renderCohortDistribution() {
  const container = document.getElementById("cohorts-distribution-container");
  if (!container) return;
  container.innerHTML = "";
  
  const COHORTS = [
    { id: "canonical", label: "Canonical Leader (260+)", min: 260, max: 300, class: "range-canonical" },
    { id: "emerging", label: "Emerging Leader (230-259)", min: 230, max: 259, class: "range-emerging" },
    { id: "rockstar", label: "IT Rockstar (190-229)", min: 190, max: 229, class: "range-rockstar" },
    { id: "expert", label: "Industry Expert (160-189)", min: 160, max: 189, class: "range-expert" },
    { id: "specialist", label: "Topic Specialist (130-159)", min: 130, max: 159, class: "range-specialist" },
    { id: "pro", label: "Tech Pro (<130)", min: 0, max: 129, class: "range-pro" }
  ];
  
  let existingCounts = { canonical: 0, emerging: 0, rockstar: 0, expert: 0, specialist: 0, pro: 0 };
  let computedCounts = { canonical: 0, emerging: 0, rockstar: 0, expert: 0, specialist: 0, pro: 0 };
  
  let totalExistingValids = 0;
  
  authorsData.forEach(author => {
    // Count existing AQS (only if present in original data, i.e., existing_aqs > 0)
    if (author.existing_aqs > 0) {
      totalExistingValids++;
      const s = author.existing_aqs;
      if (s >= 260) existingCounts.canonical++;
      else if (s >= 230) existingCounts.emerging++;
      else if (s >= 190) existingCounts.rockstar++;
      else if (s >= 160) existingCounts.expert++;
      else if (s >= 130) existingCounts.specialist++;
      else existingCounts.pro++;
    }
    
    // Count computed AQS
    const c = author.computed_aqs;
    if (c >= 260) computedCounts.canonical++;
    else if (c >= 230) computedCounts.emerging++;
    else if (c >= 190) computedCounts.rockstar++;
    else if (c >= 160) computedCounts.expert++;
    else if (c >= 130) computedCounts.specialist++;
    else computedCounts.pro++;
  });
  
  COHORTS.forEach(cohort => {
    const existCount = existingCounts[cohort.id];
    const compCount = computedCounts[cohort.id];
    
    const existPct = totalExistingValids > 0 ? (existCount / totalExistingValids) * 100 : 0;
    const compPct = authorsData.length > 0 ? (compCount / authorsData.length) * 100 : 0;
    const shift = compPct - existPct;
    
    // Shift UI
    let shiftBadge = "";
    if (shift > 0.1) {
      shiftBadge = `<span class="cohort-shift-cell shift-up"><i class="fa-solid fa-arrow-trend-up"></i> +${shift.toFixed(1)}% shift</span>`;
    } else if (shift < -0.1) {
      shiftBadge = `<span class="cohort-shift-cell shift-down"><i class="fa-solid fa-arrow-trend-down"></i> ${shift.toFixed(1)}% shift</span>`;
    } else {
      shiftBadge = `<span class="cohort-shift-cell shift-match"><i class="fa-solid fa-arrows-left-right"></i> Stable</span>`;
    }
    
    const row = document.createElement("div");
    row.className = "distribution-row";
    row.innerHTML = `
      <div class="cohort-name-cell">
        <span class="range-badge-dot ${cohort.class}"></span>
        <span class="cohort-label">${cohort.label}</span>
      </div>
      <div class="cohort-bar-cell">
        <div class="bar-group">
          <div class="bar-label">Existing: <span><strong>${existCount}</strong> authors (${existPct.toFixed(1)}%)</span></div>
          <div class="distribution-progress-track">
            <div class="distribution-progress-fill existing-bar" style="width: ${existPct}%"></div>
          </div>
        </div>
        <div class="bar-group">
          <div class="bar-label">Computed: <span><strong>${compCount}</strong> authors (${compPct.toFixed(1)}%)</span></div>
          <div class="distribution-progress-track">
            <div class="distribution-progress-fill computed-bar" style="width: ${compPct}%"></div>
          </div>
        </div>
      </div>
      ${shiftBadge}
    `;
    container.appendChild(row);
  });
}


// Render Authors to Sidebar List
function renderAuthorList(data) {
  const container = document.getElementById("author-list");
  container.innerHTML = "";
  
  data.forEach((author, index) => {
    const item = document.createElement("div");
    item.className = "author-item";
    if (selectedAuthor && selectedAuthor.name === author.name) {
      item.classList.add("selected");
    }
    
    // Difference formatting
    const diff = author.difference;
    let diffBadge = "";
    if (diff > 0) {
      diffBadge = `<span class="score-diff-badge diff-plus">+${diff}</span>`;
    } else if (diff < 0) {
      diffBadge = `<span class="score-diff-badge diff-minus">${diff}</span>`;
    } else {
      diffBadge = `<span class="score-diff-badge diff-match">Match</span>`;
    }
    
    const rangeInfo = getAqsRange(author.computed_aqs);
    
    item.innerHTML = `
      <div class="author-item-info">
        <span class="author-item-name">${author.name}</span>
        <span class="author-item-score-comp">
          <span class="score-lbl">AQS: ${author.existing_aqs}</span>
          <i class="fa-solid fa-arrow-right-long"></i>
          <span class="score-lbl" style="font-weight:600;color:var(--text-main);">${author.computed_aqs}</span>
          ${diffBadge}
        </span>
      </div>
      <div>
        <span class="range-badge ${rangeInfo.class}" style="font-size: 9px; padding: 3px 8px;">${rangeInfo.label.split(" ").slice(0,2).join(" ")}</span>
      </div>
    `;
    
    item.addEventListener("click", () => selectAuthor(author, item));
    container.appendChild(item);
  });
}

// Filter Sidebar List
function filterAuthors() {
  const query = document.getElementById("search-input").value.toLowerCase().strip || document.getElementById("search-input").value.toLowerCase();
  const rangeFilter = document.getElementById("range-filter").value;
  
  const filtered = authorsData.filter(author => {
    const matchesSearch = author.name.toLowerCase().includes(query);
    
    let matchesRange = true;
    if (rangeFilter !== "all") {
      const score = author.computed_aqs;
      if (rangeFilter === "canonical") matchesRange = score >= 260;
      else if (rangeFilter === "emerging") matchesRange = score >= 230 && score < 260;
      else if (rangeFilter === "rockstar") matchesRange = score >= 190 && score < 230;
      else if (rangeFilter === "expert") matchesRange = score >= 160 && score < 190;
      else if (rangeFilter === "specialist") matchesRange = score >= 130 && score < 160;
      else if (rangeFilter === "pro") matchesRange = score < 130;
    }
    
    return matchesSearch && matchesRange;
  });
  
  renderAuthorList(filtered);
}

// Select Author and Show Scorecard
function selectAuthor(author, element) {
  selectedAuthor = author;
  
  // Highlight in sidebar
  document.querySelectorAll(".author-item").forEach(item => item.classList.remove("selected"));
  element.classList.add("selected");
  
  // Display detailed area
  document.getElementById("no-selection-state").classList.add("hidden");
  const detailsContainer = document.getElementById("scorecard-details");
  detailsContainer.classList.remove("hidden");
  
  // Fill text details
  document.getElementById("author-detail-name").innerText = author.name;
  document.getElementById("author-detail-book").innerHTML = `<i class="fa-solid fa-book"></i> Primary Book: <strong>${author.title || "Unknown Book"}</strong>`;
  document.getElementById("author-detail-bio").innerText = author.bio || "No biography available.";
  
  // Fill Social links
  const socialContainer = document.getElementById("author-detail-social");
  socialContainer.innerHTML = "";
  if (author.links) {
    const platforms = [
      { key: "linkedin", icon: "fa-brands fa-linkedin-in" },
      { key: "github", icon: "fa-brands fa-github" },
      { key: "twitter", icon: "fa-brands fa-twitter" },
      { key: "website", icon: "fa-solid fa-globe" }
    ];
    platforms.forEach(p => {
      const url = author.links[p.key];
      if (url && url !== "nan" && url !== "") {
        const btn = document.createElement("a");
        btn.href = url;
        btn.target = "_blank";
        btn.className = "social-btn";
        btn.innerHTML = `<i class="${p.icon}"></i>`;
        btn.title = `${p.key.toUpperCase()}: ${url}`;
        socialContainer.appendChild(btn);
      }
    });
  }
  
  // AQS value fields
  document.getElementById("score-val-existing").innerText = author.existing_aqs;
  document.getElementById("score-val-computed").innerText = author.computed_aqs;
  
  // Classification badge
  const rangeInfo = getAqsRange(author.computed_aqs);
  const detailBadge = document.getElementById("author-detail-badge");
  detailBadge.className = `range-badge ${rangeInfo.class}`;
  detailBadge.innerText = rangeInfo.label;
  
  // Variance layout
  const varianceBadge = document.getElementById("score-variance");
  const diff = author.difference;
  const arrow = document.getElementById("comp-arrow-icon");
  
  if (diff > 0) {
    varianceBadge.className = "score-variance-badge diff-plus";
    varianceBadge.innerHTML = `<i class="fa-solid fa-circle-arrow-up"></i> +${diff} points higher`;
    arrow.className = "fa-solid fa-right-long diff-plus";
  } else if (diff < 0) {
    varianceBadge.className = "score-variance-badge diff-minus";
    varianceBadge.innerHTML = `<i class="fa-solid fa-circle-arrow-down"></i> ${diff} points lower`;
    arrow.className = "fa-solid fa-right-long diff-minus";
  } else {
    varianceBadge.className = "score-variance-badge diff-match";
    varianceBadge.innerHTML = `<i class="fa-solid fa-circle-check"></i> Exact Score Match`;
    arrow.className = "fa-solid fa-right-long diff-match";
  }
  
  // Render Chart
  renderRadarChart(author);
  
  // Render Dimension breakdowns
  renderDimensionsBreakdown(author);
}

// Render Dimension Radar Chart
function renderRadarChart(author) {
  if (radarChart) {
    radarChart.destroy();
  }
  
  const labels = [];
  const scores = [];
  
  for (let i = 1; i <= 12; i++) {
    const dimId = `D${i}`;
    labels.push(`${dimId}: ${DIMENSIONS_MAP[dimId].name.split(" ").slice(0, 2).join(" ")}...`);
    scores.push(author.dimensions[dimId]?.score_percent || 0);
  }
  
  const ctx = document.getElementById("aqs-radar-chart").getContext("2d");
  
  radarChart = new Chart(ctx, {
    type: 'radar',
    data: {
      labels: labels,
      datasets: [{
        label: 'Dimension Score %',
        data: scores,
        backgroundColor: 'rgba(0, 242, 254, 0.15)',
        borderColor: '#00f2fe',
        borderWidth: 2,
        pointBackgroundColor: '#4facfe',
        pointBorderColor: '#fff',
        pointHoverBackgroundColor: '#fff',
        pointHoverBorderColor: '#00f2fe'
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      scales: {
        r: {
          grid: {
            color: 'rgba(255, 255, 255, 0.08)'
          },
          angleLines: {
            color: 'rgba(255, 255, 255, 0.08)'
          },
          pointLabels: {
            color: '#9ca3af',
            font: {
              size: 10,
              family: "'Inter', sans-serif"
            }
          },
          ticks: {
            backdropColor: 'transparent',
            color: '#6b7280',
            font: {
              size: 9
            },
            stepSize: 20
          },
          min: 0,
          max: 100
        }
      },
      plugins: {
        legend: {
          display: false
        }
      }
    }
  });
}

// Render detailed breakdown list for dimensions
function renderDimensionsBreakdown(author) {
  const container = document.getElementById("dimensions-container");
  container.innerHTML = "";
  
  for (let i = 1; i <= 12; i++) {
    const dimId = `D${i}`;
    const dimData = author.dimensions[dimId];
    if (!dimData) continue;
    
    const card = document.createElement("div");
    card.className = "dimension-detail-card";
    
    card.innerHTML = `
      <div class="dim-card-header">
        <div class="dim-card-title">
          <span class="dim-id">${dimId}</span>
          <span class="dim-name">${dimData.name}</span>
        </div>
        <div class="dim-points-val">
          ${dimData.points} <span>/ ${Math.floor(dimData.weight)} pts (${dimData.score_percent}%)</span>
        </div>
      </div>
      <div class="progress-track">
        <div class="progress-fill" style="width: ${dimData.score_percent}%"></div>
      </div>
      <div class="dim-justification">
        ${dimData.justification}
      </div>
    `;
    
    container.appendChild(card);
  }
}
