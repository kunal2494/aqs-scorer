import json
import os

discovered_links = {
  '"Miss Tonya Chernyshova" linkedin': [
    {
      "title": "packtpub.com - Miss Tonya Chernyshova",
      "url": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFUviKBKlbN52rSDXoCqV_FmdO55LO7FjR9PUwRKMX_nbCLls6jXeG4iTHlp8HMqRGjizChVHvRGupN_BMLVbczPcFzKM5x9AuQ4b9HT-4tugYzK3fHw6l8LdNWHt5wZAQ88hbh_gQ4deQGvLiNszQfXlyQMF4hsTGBTNo-Nct_GWDCZvTmfJNy2L-xFu_WknHsfo_DPDwbNJHyAZfiVRWwsuXL9RGZ9NWo_4zUqCQ8IxhWSeG2PwCY5MO5m4MWjuAc78H-z8og4wj_SKIweL15Qkf8ZuabQGYm7zeDgqcAeAvs6WWdgyRfEeTkNPY=",
      "snippet": "It appears you are looking for Tonya Chernyshova (often referred to as an experienced Data Engineer). While there is no single \"Miss Tonya Chernyshova\" LinkedIn profile, Tonya Chernyshova is a known professional in the data engineering field. She is notably a co-author of the Azure Data Factory Cookbook (Second Edition). Professional Background: She is a Data Engineer with over 10 years of experience, including previous work at Amazon. His expertise includes data modeling, automation, cloud computing (AWS and Azure), and data visualization. LinkedIn Presence: You can typically find her profile by searching for \"Tonya Chernyshova\" on LinkedIn."
    },
    {
      "title": "scribd.com - Miss Tonya Chernyshova",
      "url": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH6VWluEz6uJWnnInmW_vcXrFCqPzc65PRt_wrglr9rgUlBpPdHhTFLOe6W4ewTkQ6481y3jxAEcqkdGxwVQV03SnzgnauIKOizLe6QVpsDxMtJJ1Bj7gki3IVGOU1qSdAV7dhh_LozdslOo89gyM6Jl_AuxqgGxTlbS71MjT6bJ5pzuJgXFPS1Li-wQ1IEd_wVO4CchRz7IZweBmxjY0mXq5mZJmT9pQ==",
      "snippet": "It appears you are looking for Tonya Chernyshova (often referred to as an experienced Data Engineer). While there is no single \"Miss Tonya Chernyshova\" LinkedIn profile, Tonya Chernyshova is a known professional in the data engineering field. Professional Background: She is a Data Engineer with over 10 years of experience, including previous work at Amazon. His expertise includes data modeling, automation, cloud computing (AWS and Azure), and data visualization."
    },
    {
      "title": "greglow.com - Miss Tonya Chernyshova",
      "url": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGpbfs0xlCFI2E_3kYY32K86K4qyq9tiHaaj90N28L0ahPKBIlTjOKcCYRzGF2c8KdLpBzdIjOOM9-7h9bGSmmJAYCYi27_09IlE7jQcVW98rGH0yDdUIp8LSfEoCANHKHS-G1qfYjOclDij5l_VBWIGJ1RamCsNKOiSEoS7PIB_aELk1RGCctNyK5OlevVtaRy",
      "snippet": "She is notably a co-author of the Azure Data Factory Cookbook (Second Edition). Publications: She is credited as a co-author on the Azure Data Factory Cookbook, alongside Dmitry Foshin, Dmitry Anoshin, and Xenia Ireton."
    }
  ],
  '"Sarah Cook" linkedin': [
    {
      "title": "legal500.com - Sarah Cook",
      "url": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEbWYWy1pUzKnGgwO0Am4fR1TdnmUlDhqZKbKnfT4nLq2u-x24WqJGDEEkBOgzNu1937jhwBIch1w-tx3VDTL3gy7q-nV8se2aJAeTbIGZFH-QUNyU9w9KMlgdKE_ErKvPgOen9gvjAssa9NBvKRzXC3RuJULKohyRU_Cnu-QqcP6SAmHOwnXYx3mI=",
      "snippet": "Sarah Cook (Forsters LLP): Partner and Head of Construction at Forsters LLP in London."
    },
    {
      "title": "frpadvisory.com - Sarah Cook",
      "url": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGhHv-QkAN9KRxbFMM7GMeAk0IE9Vf2UaQPa_9JkcP47CPDtxliRI5AWAa26MPZqwTZfhfpQdJOwHcxuGMaRGdwGLr1HHzOAyzhEKwRaB_blpyMNzPGC65B6AjLgF_g9EIdVCSpfYvfi0fv7g9XufIr0g==",
      "snippet": "Sarah Cook (FRP Advisory): Partner in the Restructuring Advisory team based in St Albans, UK."
    },
    {
      "title": "unitar.org - Sarah Cook",
      "url": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEcehuyr3mRRdkkt22Ol3LL17I-wNPQrdELLj7JKI68lvG3kr0Sy8OWJMAztMdoU_0_UYo2G-Tz6gqRSpiHpXaXgpNqp2AT6loQ7JpLy5UIMTHXpWA8-6NcdG3XKqBBHCv_W8gMNkkxbWcNOdWkD7cLwR1TiDkaomY-YO8C",
      "snippet": "Dr. Sarah Cook (University of Nottingham Ningbo China): A Professor and former Director of the UNICEF Office of Research-Innocenti."
    }
  ],
  '"Leron Zinatullin" linkedin': [
    {
      "title": "zinatullin.com - Leron Zinatullin",
      "url": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGYngFWWe9AnECxw82r6s5H-0dmanfC6jKI2vFealw2gmT-nnI9zjGBJHisx26aGrYhw-zoac14qFhOI1P-cdhWYShMalEnaxJymadX17W_v5QXvQ==",
      "snippet": "He is a well-known cyber security executive, author, and speaker. As of 2026, he serves as a CISO in the FinTech sector (notably associated with Constantinople) and has been recognized as one of the Top 10 Cybersecurity Leaders in Australia."
    },
    {
      "title": "6degreesmedia.com.au - Leron Zinatullin",
      "url": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEDWVcoCK9_BIJghDOkN0H-IDAK6hIWew6FBe0F4AX13PKkvPdyWkdKm3Z6xmYI9OzNu5WvGmU62VcazWYbVE4S1u5KSCGa6Jt_NZVLp7F7J8-NqkQ8OHGE-kIT8ut7X3GNQvhwPw0W1iUTTbqm-UCAN5eAekXcRmNj",
      "snippet": "He is a well-known cyber security executive, author, and speaker."
    }
  ],
  '"Sophie Hussey" linkedin': [
    {
      "title": "iil.com - Sophie Hussey",
      "url": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFdL8IxmOI-Vp474-iriPIhvPpidbYOEu9ZZ66x_w9GRyBvndKe9ttcCsQc2fWNAydnZY8N-qe2_AIcxTw42PF7ftAmxZ_rsI1AaAAkzeo8_Cp89p6M5DtVyVo9e9rIbqIJ",
      "snippet": "Sophie Hussey is an experienced technology professional and the Director of Lapis Consulting Services Ltd. Her work focuses on IT Service Management (ITSM), IT leadership, strategy, and mentoring. Consulting & Leadership: Nearly 25 years of experience in the technology sector, transitioning from a technical career path to service management and leadership roles. Expertise: She specializes in supporting organizational growth, driving service excellence, and fostering human-centric leadership. She is an ITIL4 Managed Professional. Advocacy & Community: She is active as a STEM Ambassador, a Women in Tech mentor, and a Fellow of the Royal Society of Arts (RSA). She frequently contributes articles and speaks on topics such as neurodivergence in ITSM, authentic leadership, and service management."
    }
  ],
  '"Alan Shipman" linkedin': [
    {
      "title": "promachbuilt.com - Alan Shipman",
      "url": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH2ZOkEZOVKUX642fd0nxj5MBrwK0DE9OkNSFFcjqZAZjaUd46RX1HcM0a1zaov5srGBJeMvxVZoCLVJ5bQg-DGFjiB7WnNQ0vZm9u73mCmzfnrrlGAl6aaoePcY8HBCah2pUakrrV-iJmuhNVDYmxxwF-f",
      "snippet": "Alan Shipman (Business Executive): He is the President of Labeling & Coding at ProMach. You can find his professional profile and updates via the ProMach website."
    },
    {
      "title": "open.ac.uk - Alan Shipman",
      "url": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEn1olIFG8hHnybW5vApg4jGwYTbWUrGurzoJGUCv9CzZuglmWRkEIKv_Gybrxjl27YmEM5C_6opoD29wgUkLtwj7VWpnHrS75sCWWSX-lLuUaBHRjTvBD3HbXF1piKGSPE629I_3a4Q0vCnQ==",
      "snippet": "Dr. Alan Shipman (Academic/Economist): He is a Senior Lecturer in Economics at The Open University. His research focuses on finance, innovation, and economics. You can find his academic profile on The Open University website."
    }
  ],
  '"Steve G Watkins" linkedin': [
    {
      "title": "coursera.org - Steve G Watkins",
      "url": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHCfYzQMukMGwkrmmxUINWS1mSSWycxAmSqfpX8ZvJcgr1OFuklz__LndneIeazkect8gsd5p4SSF_GG_F_GEtjKLZsXHPX4v1jagqJVkzDq0W2-786t-g7e9kvV-Q3ePnUFdy8KnghKd6P4gMBX1ZGFgsVCeOrUMGdqjeKA5TaFDjIHdrFtuuwAxomkijgILeKRToVv-c=",
      "snippet": "Steve G. Watkins is a known author and expert in the field of information security, particularly regarding ISO 27001 standards. If you are looking to connect with him or verify his professional background, you may consider: Searching LinkedIn directly using the filters for \"People\" and refining by \"Information Security\" or \"IT Governance\" to see if a profile matches the author of Information Security Risk Management for ISO 27001/ISO 27002."
    }
  ],
  '"Kerem Koseoglu" linkedin': [
    {
      "title": "github.com - Kerem Koseoglu",
      "url": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGQ_J99mnt7XUlqquxzGppIgfM08oPfWg02nCiuThicuw51wJ0UEdVLAHULpDVr2juaw9EDUvDmyWjCm6P_JTvvA_FM2wbLuQaKzDkb1HQKfYb8MbiA_g==",
      "snippet": "Dr. Kerem Köseoğlu (Software Engineer/SAP Expert): A freelance software engineer and technical author specializing in ABAP, Python, JavaScript, and Swift. He maintains a personal website at keremkoseoglu.com and his LinkedIn profile can be found at linkedin.com/in/keremkoseoglu."
    },
    {
      "title": "keremkoseoglu.com - Kerem Koseoglu",
      "url": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGeIsoTyYImk7XqrSiR50OkAfgodhQB2NrfBcj39DQJ3ymAROJxPoMFwoYWEFRt9evGgTMKrj37bL6vTtlA2REj9342ywjwykeN8CWO1f-_6g==",
      "snippet": "Dr. Kerem Köseoğlu (Software Engineer/SAP Expert): A freelance software engineer and technical author specializing in ABAP, Python, JavaScript, and Swift. He maintains a personal website at keremkoseoglu.com and his LinkedIn profile can be found at linkedin.com/in/keremkoseoglu."
    }
  ],
  '"Kristian Köhler" linkedin': [
    {
      "title": "source-fellows.com - Kristian Köhler",
      "url": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE3o9mv3-esJpA7LMGyAPCbxk_trWj1-vFATtzTVC1XXgcjFeQUccffajM0hcZ3nEJg19nRaptzQO0MLfPBzikzj0bCyennC2wrQ3UD5ug79K_CWashet3zCm2XJcwFecJCOQVHhuDy8MHgUQk=",
      "snippet": "Kristian Köhler (Software Architect): He is a software architect, developer, and the Managing Director of Source Fellows GmbH. He is also an author who has written books on software architecture and design, such as \"Software Architecture and Design – The Practical Guide to Design Patterns\". You can find his professional profile by searching for \"Kristian Köhler Source Fellows\" or \"Kristian Köhler software architect\" on LinkedIn."
    }
  ],
  '"Inga Strümke" linkedin': [
    {
      "title": "wikipedia.org - Inga Strümke",
      "url": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHXxYOPS2tZ7c4H5RpNwR4i37KX7CvLEKxF7YtkDC6NiPKHUKk0kCVUrYR-KH-Jm6HZjV5E3p1G-MXKqhi8GVQeWKqHjGesAYlTHK4UxdXdvMekFEw4obGOCzEoFNEvTRyosYxqtw==",
      "snippet": "Inga Strümke is an Associate Professor and researcher in Artificial Intelligence at the Norwegian University of Science and Technology (NTNU) and the Norwegian Open AI Lab. Key professional details: Research Focus: She specializes in machine learning, explainable AI (XAI), and AI ethics. Background: She holds a PhD in particle physics and previously worked as a consultant in responsible AI and algorithm auditing at PwC. Public Outreach: She is a well-known public speaker and author of the award-winning book Maskiner som tenker (\"Machines that think\")."
    }
  ],
  '"Helmut Vonhoegen" linkedin': [
    {
      "title": "cb-india.com - Helmut Vonhoegen",
      "url": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHGyU1TiQIPgfkA0HJ33_T2H3trFAwQo1ZxORPLE0J4KdLSGYeWUmuK4HGDUQKUD7TfdUtV4roIHCd6XJfMe7uKvUkies9Qr6bhs9Rd03r6Ryg7SK-knoaNVRmhOfqdY7JsDa648z3Mgs9nv_i-qmtNU6Y=",
      "snippet": "Helmut Vonhoegen is a freelance author and IT consultant known for his extensive work in technical writing, particularly regarding Microsoft Office, Windows, web programming, and XML. Since 1992, he has authored over 80 books and numerous specialist articles."
    }
  ],
  '"Bert Gollnick" linkedin': [
    {
      "title": "packtpub.com - Bert Gollnick",
      "url": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGkqPvbv5hnJzPZ_V2Jx6RFlb63r8kW-bxKuhX0c_krUN5oRql0MmA3o2JkoTsW6ZBKWdQVv3XwQULaoXkIxh5UnhGnqrkmnjSqOkdivMkTfvdqy0wfxjkOnTdMjLCIeleFxpmEVw9iRd9jLUTVGGjAG67kB1Nwy_MTlcRo0GJuHBL7VpY6nXIvtAnQ-UwCgCWzzIJcMVi6Ns8TBc_r5Rsk6b-7D6AaPOz2upNaG_r49FKVGuSSMYyYXIfo-ZDSPNKeL8Ykl8-GtfVRpjOpqnRx",
      "snippet": "Bert Gollnick is a senior data scientist with extensive experience in the renewable energy sector, specifically wind energy. He currently works for a major wind turbine manufacturer. Expertise & Teaching: He has spent many years teaching data science, machine learning, NLP, and PyTorch. He is an author of several technical books and courses."
    }
  ],
  '"Dr. Joachim Steinwendner" linkedin': [
    {
      "title": "cb-india.com - Dr. Joachim Steinwendner",
      "url": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFwjxM_e3GYUpmbtC14kPJP9LvUFThi0O56s5V4m0BuTHwncp_QPzzK-bgKcVNduILvvTizCyZWTAYCMIXvhWwdFiwbSgVnFq3NLyaFJwdif9Mqdz-t4jVXWKdJqdwhXzDQ1fVMyBPG51XgMasRgkVfzn5RAV-wEx4Su9mXFOpThjE50beTSFqPi6Ep7NjsRFkCRWgIDmPq9In9BB8G1FJGqejx3aoWhKJpvG8KBD7bDdiBVaK7rAx1",
      "snippet": "Dr. Joachim Steinwendner is a professional with extensive expertise in data science, machine learning, and deep learning. Author & Expert: He is a published author in the field of technology, having co-authored books such as Programming Neural Networks with Python."
    },
    {
      "title": "heise.de - Dr. Joachim Steinwendner",
      "url": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHHCAkGqZggVApEGCL_i6iRaxrcQjf2aonitZP-VexKrbQW-fb5TBCQ89FPR4vyBeOC5PgwxslWuy5ZbBd1Jg3BDyaHArRQyeDTk9l3kJ1J8CeaYLOP6Iy12cJg4ZlZk1IZXVbAgxu4JpmjtoSEHnCrKj-2XZ6JhrmPLRZ5zvsoTRISSg==",
      "snippet": "He is currently active as a lecturer and research lead, notably serving as the Research Field Lead for Digital GeoHealth at the Fernfachhochschule Schweiz (FFHS). Industry Presence: He frequently appears in professional publications, conference programs, and as a subject matter expert in data science."
    }
  ],
  '"Dr. Roland Schwaiger" linkedin': [
    {
      "title": "packtpub.com - Dr. Roland Schwaiger",
      "url": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFSjn4zN_Z25NFi1LdxI3nQyi06PGnWIZFgdZ6vdhasUGSGSaiHUvLf1Bu-MIwI_uNmYKRHfQ7_S_ENGvOXmZZ2A-7ecJ2mwJWlnH9jmwU4V6AXpVaj6-YeYCM-zUS0MECkMRUW3f14NEBLXLRHAvIJwZqfCMEz_ZfOtFgBhc_E3KLzlU_3is8IL2bvgOqPdUFpOg==",
      "snippet": "Dr. Roland Schwaiger is a software developer, consultant, and trainer with a PhD in mathematics. He is known for his work in the fields of artificial neural networks, image recognition, and IT education."
    }
  ],
  '"Mohammad Nauman" linkedin': [
    {
      "title": "sciopen.com - Mohammad Nauman",
      "url": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFGJjFxA7LJM8efksVtAsuBXkpTNtHPzaNnsQ-SuvmfZzssndIQ1w1S0-23HdavcDmkNDt1q71-N3m4mfBZv-ky67uVJ9FqJ5s1MITayrxkuJ3P1SJnpLKdn2TCFXfoIiXc1Im7JJyAUPxYq2Qj8bA=",
      "snippet": "Mohammad Nauman (Cybersecurity Researcher/Academic): An academic and researcher with a PhD in security and privacy. He has worked as an assistant professor at Effat University in Saudi Arabia, focusing on adversarial machine learning, cybersecurity, and artificial intelligence."
    },
    {
      "title": "recluze.net - Mohammad Nauman",
      "url": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE4QHNqO-mSjULA5qYmsGv95a-RL0mCVAERFsfwZ3kXIEnKQcrlWWG9wAZ9VG5phV4IHt31M4lw8FlZuMimOoKiEgwgqwdOExwTaenzXLmZ4N7KKQ==",
      "snippet": "Mohammad Nauman (Technology/Engineering): There is a professional profile associated with the handle \"recluze\" that lists a LinkedIn URL as linkedin.com/in/recluze. This individual is known for technical writing and content related to secure systems and hardware."
    }
  ],
  '"Michael Kofler" linkedin': [
    {
      "title": "packtpub.com - Michael Kofler",
      "url": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGDsxmMprjWLRb108hTz0gdV58UCEZDLmFPfPYQO7p4OeE4vZ9dawAS54FQyfJwAo4XmlZ89zdBgN_ewJ88WIb2v0ona2_YDxZkqRSGKX4xFMIFz6XYhYGuA0NnqrnphUUUKEJrU0PTR36pLNEXeuAJ75Sb9htgZk0Asgak0BVkI3QL9f2pj62N4G1V1tYjfJWtES4MWNtomPJ8HMoNITsppfgaJe863rdECsGXpxDZAdLqxM9rZxlv7cChkq2Cc3R75rgE5pcn",
      "snippet": "Michael Kofler (Computing Author): A well-known author, programmer, and Linux administrator. He is recognized for his books on Linux, Docker, Git, and various programming languages and teaches at the Joanneum University of Applied Sciences in Austria."
    }
  ],
  '"Nouman Azam" linkedin': [
    {
      "title": "udemy.com - Nouman Azam",
      "url": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQET8GCcjcy5mRP9VcKk86POiPm0VVeKZj7zh0Rwl7unWaKYkNg4iFWCeSu_mOFj_Q0_EDNAuP4ybZwIhBrB7Kmk5oFy0GX7TCIykhilnbNdhrFgr8PlQ70MbprmUw==",
      "snippet": "Dr. Nouman Azam is an academic and computer science educator. In addition to his academic role, he is a well-known online instructor who teaches courses on programming—including MATLAB and other computer science topics—to a large community of students."
    }
  ],
  '"Bernd Öggl" linkedin': [
    {
      "title": "rheinwerk-computing.com - Bernd Öggl",
      "url": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFEMvTZMEH6E799H0TwXCugtGjgW34NYqzlTjqGz8DQCgUpV0joxCJf-G_0jZRE22l2wzN5b6USLgQyQNQVXTCzgNhBPhqs4vPIyF-cVJk1PWoRcnH0aGN7QAA11ixlpsFMhYthKLAEDRmfjJJrkQRdnqI3EONDPqrWrA418BL0",
      "snippet": "Bernd Öggl is an experienced system administrator, web developer, and author based in Austria. Expertise: He has been working in web development and system administration since 2001 through his company, webman.at. His technical focus includes Docker, Git, AI-assisted coding, and web technologies."
    }
  ],
  '"Sebastian Springer" linkedin': [
    {
      "title": "packtpub.com - Sebastian Springer",
      "url": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHYXRVDH_Es_LZ6kAX4ZACPEfbsF37uRSWdnO0Z7Y7DYeVCy8sxHingbJCVyXO-fkpSGQvf0qAGS0CBuIkMalp9KNlppR8auvqCdJCqfz_5EcFYWc_4xGC5Lwh1Ui5Srl5wRB5ODGhbHCeZoXw1FxHpdmKuFD_gM27FA8QO5YxaCfrMES4r4YKBv3eMAl18vx_q6r-US1OTM5G-fU6ZoT8-vIHaEfrlzgAjh_6NOybxmhElhjD3QXOo",
      "snippet": "Sebastian Springer (Software Engineer/Author): A JavaScript engineer at MaibornWolff and an author of technical books (including Node.js: The Comprehensive Guide). He is well-known in the German web development community."
    }
  ],
  '"Axel Miesen" linkedin': [
    {
      "title": "xing.com - Axel Miesen",
      "url": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEjvCav5wusmOT7mLkycDZCp2ZQ4-broY5PGU8GM9u2Hq8R02AvYVNHnzPaZ5xs8ch5e8B2Z79qSy8HVQ3lAguzdWFTF2KJz3nhpJyg8INTogynCHpx-CkmwPO5uMmX",
      "snippet": "Axel Miesen is a German IT consultant, author, and trainer, primarily known for his expertise in Linux, DevOps, and Ansible. Expertise: He specializes in Linux solutions, system administration, and automation, particularly using Ansible. Author: He has written several books on IT topics, most notably Ansible: Das Praxisbuch."
    }
  ],
  '"Christian Wenz" linkedin': [
    {
      "title": "techorama.nl - Christian Wenz",
      "url": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH5EQJsKQBWwTJnOoD8s7Gr5Zyk5GfqGcoZpDRo9chW-9c3WzlW3RQVqdUb3umQl2K7yfEYe5mgcsdKo3GUahnE6kbvtQgjW29bkE7Ue7fg56Og6UM1mYBT2uoF8H2Efzsf4x5JdIM0K3I2QpSP4w==",
      "snippet": "Christian Wenz's professional profile can be found on LinkedIn at: https://www.linkedin.com/in/chwenz/ (Note: This is the common profile URL for Christian Wenz, who is a well-known software architect, consultant, and author specializing in web technologies and security.)"
    }
  ],
  '"Tobias Hauser" linkedin': [
    {
      "title": "learntec.de - Tobias Hauser",
      "url": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH4dj1e6gfknSSh1fjZNbRCKdVA3Px_gIyFv5ZOJYIsSYDP-Hbc649WGnsKmnYyyim23wpXXJtnpGbl2VmZkrfQBIbajZDyW4rZfkEwFm70HPeIzSFzRoLA8PIsUhrsjGaEK69HCPA--vwLYHUZAQqtb3ae5R9Bo0qiUAqTx5GXdar_rPPc5319jUDuCHI3Ku3cqySAI2Kp5boUS3lRLg==",
      "snippet": "Tobias Hauser (E-learning/E-commerce Consultant): There is also a Tobias Hauser who is an author, trainer, and consultant specializing in e-learning and e-commerce. A LinkedIn profile for this individual can be found at linkedin.com/in/tobias-hauser/."
    }
  ],
  '"Mr. Bin Zhang" linkedin': [
    {
      "title": "brunel.ac.uk - Mr. Bin Zhang",
      "url": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEHg70HYoWKnEoylGiEqmJkSo4ArfGAvV5nz-7FegAjO7TUrDZ8nmQTjXEQAXGeeAQ6yhvVPTISGNearPQ4nuzF4TT4IAt0_23xPU_arBG-6-BHxp-cC3VAfkaNKRVdPA==",
      "snippet": "Dr. Bin Zhang, a Lecturer in Additive Manufacturing at Brunel University London."
    },
    {
      "title": "mbzuai.ac.ae - Mr. Bin Zhang",
      "url": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFmA34YuHfMM_j4nJY6EbFBcv216iF8VWvk8b-xznbARGSyHqf_jjD03EDGiL4iJRv3D91hA7s9H8OC-JIy-Aol4XHAhX4vHosxGbBKNYVKZoVpahhbT2YQELEUKK_ZSaZYkDk=",
      "snippet": "Bin Zhang, an Assistant Professor at MBZUAI."
    }
  ],
  '"Zhenyao Wu" linkedin': [
    {
      "title": "zhenyaowu.com - Zhenyao Wu",
      "url": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGHAvNByd2fc_f5fnFqMDhz_5GlBN6SQHOqqu314WAqzbUEccAqTNuZf_h0asXdatH05d8tgK8CzMVYZ0mF3N0pLltlXIJdxwii430=",
      "snippet": "Zhenyao Wu (Researcher/Engineer): He is a researcher with a background in computer vision, deep learning, and image processing. He has been affiliated with the University of South Carolina and is currently a principal engineer and researcher at Honor Device Co., Ltd."
    }
  ],
  '"Mr. William Mayhew" linkedin': [
    {
      "title": "justia.com - Mr. William Mayhew",
      "url": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG8PqFT-xilSfktnVWhqdR9uumEwNEZwezZMwtBjm2nppIhRe9EpsVGfUZ-RXiylax271hJ8BxBNwJ7ms2GHcpZFMU3buTzS4AnfNwr18Q-OXzM1SkqS3onHSd2iAR8W5HCQCGolmoddw8tgbeaKf5Zg9ld6g==",
      "snippet": "Legal Professionals: There is a William George Mayhew, an attorney based in Florida with a background in law and ministry."
    }
  ],
  '"Thejendra B.S" linkedin': [
    {
      "title": "coursera.org - Thejendra B.S",
      "url": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEeFUULs5iJE05may2tkQGFUfErk3vwmN_HhcUQO9O5lgE3xj_O9xx_c_LK1zE0PXqZz4A55PxdI3dXf7A3_NrxoZAFSeztspB1sgM8p-HRoJgQSRnnc7-P2O-y7NcbHxhqCs77xGPEPtlEYBOVTq8CIvwEqfw4yC8FPg==",
      "snippet": "Thejendra B.S. is an author known for his work on IT service management, disaster recovery, and business continuity. Information regarding his professional background is primarily associated with his books and contributions to IT governance literature."
    }
  ],
  '"Mr. Daniel Levy" linkedin': [
    {
      "title": "cobsinsights.org - Mr. Daniel Levy",
      "url": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE-eVNRRsLdHmMboWndsXFmiXHCVAECx0fa7-p84naIE94Wi0E-_whCF8EXKi6Jz6Wkn13UpPJGEoB9OprToDEhLqWrltRQVeYm3U8LHZNGFhvtEVC_YGcLEBpmrcvszQ==",
      "snippet": "Daniel Levy (Tottenham Hotspur): The Chairman of Tottenham Hotspur Football Club. He is a well-known executive in the sports industry."
    },
    {
      "title": "wikipedia.org - Mr. Daniel Levy",
      "url": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFCCfcjKXNwCG-q2FqBsIyHm38rWOWjAXOWfv8BZ_TV4aGzDxumnZ3l50IIatv-PEufwR1oE4IT3AqRnpwNfphoGSyubH6PnfBqIeujbOewLqw_D3aPICXcK65Hy5CYemx3oDK0Zthln-QuET0jK50aWVp2",
      "snippet": "Daniel Levy (Political Analyst): An author, commentator, and former Israeli peace negotiator who serves as the president of the U.S./Middle East Project."
    }
  ],
  '"Eduardo N. Sanchez" linkedin': [
    {
      "title": "ipgbook.com - Eduardo N. Sanchez",
      "url": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGfpzwVvpnBI5X0fSEJ-3Eawnb6Jh2bxCDR9Rhc0Awe9pPkt-dAZACoDyeV-QQamIyMCWRP9dsRUtClZQ9UbbEvwoFrXzfApFnzMb9GyHlRITRXZylkXbd9CkEINDi0uRulzznWnihJyr3ijguz_vxMzAh1_WnxFd5fDoNY4Fx5YIpoZ-pBrofzDJMy0t-KkysyQpO4ELAE2cIv3NkrDbmvOSguG-uYRg==",
      "snippet": "Eduardo N. Sanchez is an author known for his technical books on Microsoft Excel and VBA programming, such as Programming PowerPoint With VBA Straight to the Point. Professional Background: He is a Brazilian Chemical Engineer with extensive experience in programming languages including Fortran, Basic, Algol, Pascal, C, and VBA."
    }
  ],
  '"Mr. Benjamin Frain" linkedin': [
    {
      "title": "donyad.com - Mr. Benjamin Frain",
      "url": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHDiJrVdvCdDnAl1rNn-ZLQxtu9ktu-NjaS7hyP-kiyqsJ0GiX4dj-sIfL0u_1ljuiPQu9xfSHEGkblfCg0duSR5IG-fOBEbWgvy48BCSubFbKdOe-8CXi8vFU50BIWPkAwPGUUvIpMqQt2J2I5JDYwIPBqWa-n2Z0yp3rQ7435KC-Fvcoyc3O5YvvFoeLP08xu0gNBGH8dfg==",
      "snippet": "Benjamin Frain is a known author and educator in the field of web development, particularly recognized for his work on HTML5 and CSS. While his video courses and instructional materials are widely distributed, there is no public LinkedIn profile that is definitively confirmed as his personal professional page."
    }
  ],
  '"Robert A. Clark" linkedin': [
    {
      "title": "husson.edu - Robert A. Clark",
      "url": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH4IHWGMPzXC3nVtKcXgpvvaDsEZ8RA3I30qD4np-_Liw5lEtjSRSnV_3m21qDoTcZyPz-lNpA6YDX12jF9w3vTtzgzkZJoftnKGdlU4dS-FlhOu6bUnuWTF6-b6dKcClq0NYu5oP6TkvJtwC_l_yDsS8Sum08I7a7xbh6_XFS0",
      "snippet": "University President (Husson University): Robert A. Clark, Ph.D., serves as the President and CEO of Husson University in Maine."
    },
    {
      "title": "alertfind.com - Robert A. Clark",
      "url": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEz2GLNdYu0_Iss5_bd64N9kFWKWqnKeunVIKOQkwb_uivWlhlL_ZcX_737_0iK0F1IMBM3yfqeGY1IOETVu7Wy_bpq5NvoDQn_QM4_qbavTqLVhWAcM3EcPvBhgb-Qy6yiGaQPAZwaeYr1CA==",
      "snippet": "Crisis Management Expert: An expert in emergency preparedness and crisis communication who has authored books on the subject."
    }
  ],
  '"Alan Field" linkedin': [
    {
      "title": "tracxn.com - Alan Field",
      "url": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEQtPceXG9Y30GRp7pGQFEr7GMxO4Yk4fD9aJneOxT_JnTokD8CtHVMSUQOsYU86EF4sBk1zlk35qauBIDmbFctdQ6-vuDqvITVnsy2BOB4cXahrVjPfaJHTP6t1V8qBGEZ2xlJZ97SRBbnl03YET9A69AURDHzW-yCpnVg7o-zye-7IMjCUAglRA==",
      "snippet": "Sixgill Co-Founder: Alan Field is a co-founder of the company Sixgill."
    },
    {
      "title": "alanjfield.com - Alan Field",
      "url": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHX964N65gcwS9rplNBPG3iZ8LAfkH-l0kfpB2SWH89Flr0Vwrm5Xq0HJ-zFkeGlmT-EgHMTpsj-K93ckoJaJ9Ul2VH1vNseAa-vbmIdHFkS_EPByyj",
      "snippet": "Author/Screenwriter: Alan J. Field is known as an author of science fiction and political thrillers."
    }
  ],
  '"Naeem Sadiq" linkedin': [
    {
      "title": "plexusnc.com - Naeem Sadiq",
      "url": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFN9HnsY4nTSMFdu_C8u2hI263Ceo4Scw5nw3fgcEuqmljmrojJOs-coHPnDfDqwZ6pl2SxOWNiO6LyQgdVn419bsqnQngDs09s8jXxRevQ_4kFKmUltYLxX0gpSofSmDqYDA==",
      "snippet": "Dr. Naeem Sadiq (Neurologist): A prominent neurologist based in India, known for his work at the Plexus Neuro Centre in Bengaluru and Hyderabad. He is frequently featured in healthcare awards and medical news."
    },
    {
      "title": "tribune.com.pk - Naeem Sadiq",
      "url": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG_Kgm8bD9N9Bc9fVJoOp2zhXstZuWTaWxHdTcw4iUhTMg4kWvL7eUAidHD2f6niQFqdHId3B2sgiNp_OH6t2ENbXtuuzB5fV_Q0M9z_zeoJIx3--sT35lP-cjRh8FCKIBN9DMkkw==",
      "snippet": "Naeem Sadiq (Columnist/Writer): A Pakistani columnist and author who frequently contributes to The Express Tribune on social and political issues."
    }
  ],
  '"Julie E. Mehan" linkedin': [
    {
      "title": "insiderthreats.au - Julie E. Mehan",
      "url": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQERt_7eM4YnFsSikc2Rk-PZj-1RtFgR0ibltPSqEWGN3pzlQJH372zKyJrqzcUV4QtIqkubmc9rFSZAzrdDTsSVqjnWXeTeZEypuT7bWuaZErZjolCN_iO4EU1qxKGYvJGPyzTihEjfEvCQMYr7Y_po8L9LgU0=",
      "snippet": "Dr. Julie E. Mehan is an author, researcher, and expert in fields including artificial intelligence, cybersecurity, and digital ethics. Expertise: She specializes in AI ethics, insider threats, cybersecurity, and digital transformation. Publications: Insider Threat – A Guide to Understanding, Detecting, and Defending."
    }
  ],
  '"Richard Bingley" linkedin': [
    {
      "title": "qualifi.net - Richard Bingley",
      "url": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH_ei4XoAHZVnHYpo0Yi8c053kebJ6_6MdSZ7R8c2FwqMdUV5Ytig_y5M8YqaSDSvdv4tITtqynfZ5FjzXE6MSph9tg2qOKqB-CYvITa5KbgONPkm7qCbERRP8=",
      "snippet": "Cyber Security & Academic Expert: This Richard Bingley is the founding Chairman of the Global Cyber Academy and Managing Director of GBS Education Group. He is a published author on security topics, a former university academic, and a leadership consultant."
    },
    {
      "title": "theguardian.com - Richard Bingley",
      "url": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEp9fV-ccfDx0FG4V4hPHVOVHOnfx3kzbig0LFIPqoT3mt7WHgUFyzCRHK0A8SZEMZVV5MD4aJ91ILEZJQJ11VW0mkEY7oEbn0FA9TjGZj6-tdVVJXyw9gOnL2dMxIQMe6ry94oVhE9-XPYhuBfDSfwqFcW6fELETElKhhFjHYJypFnqP_-YQxB9AejbdevvZjma40vlcGPlBOVGegU75Ef2sShGivXOaNAU61N68O60rTntUNs",
      "snippet": "Politician: This Richard Bingley is a UK politician who has served as the Leader of Plymouth City Council and has been active in local government in Thurrock."
    }
  ],
  '"Stephen Hancock" linkedin': [
    {
      "title": "coach4md.org - Stephen Hancock",
      "url": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFgJUY6NTuNHATkkJbL0g7L5_TIyGhUMP9t82p4Hy6BmLKqfhsbzY7fEvBXwxGYSLaOZPJPVRlL_y2QFD7_ec1CXenNiHMC-cW6lIgrWr5_ECMmQUPNRD3k9OpLViHf6GruI6MfUbar8Fc=",
      "snippet": "Leadership & Well-Being Coach: Stephen Hancock (CEC) is a coach for \"Comfortable-but-Stuck\" leaders. You can find his profile at linkedin.com/in/stephen-hancock-cec."
    }
  ],
  '"Walter Zondervan" linkedin': [
    {
      "title": "dutchitchannel.nl - Walter Zondervan",
      "url": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGly1IxYvztsTwpjBHy86qmCfnLsrxT2F__d0E8XGC-ebNhe8nIPFPOP3mqrHXHiuzeYwdEAiPY_x1aIQon9A1t84ZTIBcyrRgyeOS9OYkb4UNIZ0R2iE0gbPP1NHavYK9dzyO_ZTe1Q_A7hccSKoQJTFgtSBbOVrRAEC8_AG1wXikOOJiKLTOjVySf8XemcTM=",
      "snippet": "De IT-expert/auteur: Er is een Walter Zondervan die werkzaam is in de IT-sector (onder andere als CIO bij Pink Elephant) en die publiceert over onderwerpen als BiSL Next en business informatiemanagement."
    }
  ],
  '"Léon-Paul de Rouw" linkedin': [
    {
      "title": "tilburguniversity.edu - Léon-Paul de Rouw",
      "url": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE0PU1aS5QLbWayMXgyuBEd9kMvzlX83JvBJXRuKeoY1qJKmwARb9ft5t1Tgy5NrXGBFuI1NUCwOEUqTTPyqCnUeBbSw2OdYcfFffdqWoiDZ1smIwPMJ5CP-55L8EyDxGu0NX5TEWxDASto6xYXbG_tag==",
      "snippet": "Léon-Paul de Rouw is a senior management consultant, researcher, and author. Academic Background: He has studied organizational science and business administration in Tilburg and Eindhoven. In 2026, he completed his doctoral promotion at Tilburg University, where he has been affiliated as a researcher."
    },
    {
      "title": "bislsmart.nl - Léon-Paul de Rouw",
      "url": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHtE4b5diEiMkZ8W-whvMydlpYHeZE-crfTkX5Ke8UkfxQig3m37W4-9FpVZyLoMGj6gB9W-No06QhBGuuCsraEvuuPmDevOQwYCCygJ1AlHDaZepNRvdRmpBnyC6l74_Rin7JH6Cq73saAbQI=",
      "snippet": "Léon-Paul de Rouw is a senior management consultant, researcher, and author. Expertise: His work focuses on digital transformation, business information management, facility management, and management frameworks. Publications: He is the co-author of several books, including Digital Information Design Foundation."
    }
  ],
  '"Timothy Rogers" linkedin': [
    {
      "title": "sheffield.ac.uk - Timothy Rogers",
      "url": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH0jjiDWh7fQHwhOBYoWA1NylLP4WP6VU1dilyJD1mFbkSNbmhA48tOetENfLd9lKph2cRg_NVrvL8XgtZyKcbolpJ7Ch0_KhaeAwgHccR1yAQSacv_rlU4F01sPn9oTmpyW-nuhgUp1aQJKoC5TivYyOR9oMrCFY8bGVEHeX4=",
      "snippet": "Dr. Timothy Rogers (University of Sheffield): A lecturer in the Department of Mechanical Engineering, specializing in structural dynamics and machine learning."
    },
    {
      "title": "harvard.edu - Timothy Rogers",
      "url": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQELeZgWYIR8cihw6uSH4pxCxWpdgADIAVxjZXehg-oMQGZVDUAlFMXl-oTYUovmum75y6MIJPXyz3guOu5m0BdLBsTmZEs58S1WlH3xduEMiBL8dNWsHjiP5QVKsLwS8D0d7LYliEzKY14=",
      "snippet": "Timothy Rogers (Harvard Medical School): The Director of Disability Services at HMS & HSDM."
    }
  ],
  '"Sanjay Nair" linkedin': [
    {
      "title": "socialsamosa.com - Sanjay Nair",
      "url": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFGW47L-3fYoCe-AA1wpckd5EBNTwGSDntdzuS_ckCmiYoOQjIjiEy11UNAKqnNzALeUKYo7PQkhl5uTO97lPZT2umVlngjJznITuZ1dZgm0QzYPPeWMvXqukxzsWdOLsQT_R7DZz5oI1JhaOHvMnjft_jgQwWnTlpUflB4iOaN69xued54-4l_c5MRmOzjj0o4WBfKP0JROi-XkEkXrzOVy3DwsVly2aX0ajDNl1EypQG9rNb-UIsS",
      "snippet": "Marketing & Communications: Sanjay Nair is the Senior Director of Global Marketing Planning at The LEGO Group (as of May 2026) and has previously held leadership roles in public affairs and communications in Asia."
    },
    {
      "title": "sanjaynair.me - Sanjay Nair",
      "url": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFPkfBW-qegjsSc-UwewmpZshZYaHSO3gLJe8bwuqgg6XDiNtivamQaigd52YsBRkZBqGZltSxWX-cFo8PJgOLbCQ8h2qRipliiKEYi4RPCbO-Z",
      "snippet": "Software Engineering: There is a Software Engineering Leader who maintains a personal website at sanjaynair.dev where he links to his professional profiles."
    }
  ],
  '"IT Governance Privacy Team" linkedin': [
    {
      "title": "ox.ac.uk - IT Governance Privacy Team",
      "url": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGvsPCFCRBdkFqONTwOEEmvQeCwYqcAxah2BQvoxS4t6jxwBoij4H92TS8qJBzaZTyFxDYETMVVbaJsjhASzaErwbir5jT81qaBJrm7arP3WWkzVmk5qHPFnXTTovX1GXm_eRzsT0H5JnB8",
      "snippet": "As an Authoring Entity (IT Governance Ltd.): In many search results, \"IT Governance Privacy Team\" refers to the expert group associated with IT Governance Ltd., a UK-based company that provides training, consultancy, and resources. Publications: This \"team\" is often listed as the author of GDPR compliance guides."
    }
  ],
  '"Preston Bukaty" linkedin': [
    {
      "title": "secureworld.io - Preston Bukaty",
      "url": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHlBI0M4n1DhiEpwvr5Z4VDGc6PKSMuZVvTIosILVMk9JTGohuMGcXLcthklIYuL7myItU5I2_UUkhJ3fRYSW7vxmxr6c2QdYY1hfJ9mowUnwP6LHWnkBZnd2ZuhQJ48ZvrjtmTrLjrEB7ioog=",
      "snippet": "Preston Bukaty is an attorney and consultant specializing in data privacy, GRC (Governance, Risk, and Compliance), and information security. He has held various professional roles, including serving as a Privacy and Technology Attorney at Axiom, Senior Compliance Attorney at IntelePeer, and consultant."
    }
  ],
  '"David Barrow" linkedin': [
    {
      "title": "sessionize.com - David Barrow",
      "url": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE5cpf6tu0Ra0G8_h388Btbo0eXpVcPN8BYl5QD4lQX3rcDSb--09sxyXz9W0J5ZPgGe_Os8xfCZ_Hr52Nv5wSe0fgOU55cNE6x8PYqiz8liaxTPpcFcp9Pmi0=",
      "snippet": "David Barrow (ITSM Consultant): An Enterprise Service Management consultant, author, and recognized ITIL 4 Strategic Leader. He is active in the IT Service Management (ITSM) community."
    },
    {
      "title": "dekachambers.com - David Barrow",
      "url": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHlq2Y_33swAmb_ssDAuKYSKlkat3cG9JR3Tpw9aeWH8m4DBZChLm15Gn-mm-7VtyOf5_dfJMACExK0JPuTbuZ_cP5F-pQSgbrpV4YVR2Ovl9Hex_Q93YA-NXVhBCzZmjb8tQoli74=",
      "snippet": "David Barrow (Barrister/Clerk): A Practice Director at Deka Chambers with over 30 years of experience in civil law clerking."
    }
  ],
  '"Lee Newcombe" linkedin': [
    {
      "title": "capgemini.com - Lee Newcombe",
      "url": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHp6Etmmf5J2p1poRlZVtEpWJoG54tvADyTKBDzB2VF-usPQh8YDtZTRlZg9hvpjLsYhViNa0QZxu2z38xIPBaeS7fPH7UsR2Bj1M4bpBBA7FzLgE4jzoJNm2GYQaJXoeeflALPvuBO2jcsNxhTeCOQqmytoRy16CMPaQ==",
      "snippet": "Dr. Lee Newcombe, a security architect and industry expert. Professional Background: He is a highly experienced security professional with over 25 years of experience in the industry. He currently serves as the Global Service Owner for Zero Trust at Capgemini. Zero Trust Global Service Owner."
    }
  ],
  '"Asif Hayat Khan" linkedin': [
    {
      "title": "qimpro.com - Asif Hayat Khan",
      "url": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGa1ZCR7E8lvJBecSSzwoAJQb4pvKz-5LdwprW1MSl2s1ijWAzAbYegoIgTUjIuV2iFtDQJo0JwX2ixeKDgSTimzGM0Io6YeY-A4JQV8d2ipqYy0clltwpHuFdsu-hnrpURVh6ZtikIO8NPMg0=",
      "snippet": "Author/Professional: Asif Hayat Khan is a known author, specifically recognized for co-authoring the book ISO 14001 Step by Step alongside Naeem Sadiq."
    }
  ],
  '"Colin Bentley" linkedin': [
    {
      "title": "theadviser.com.au - Colin Bentley",
      "url": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG0AVK89KZSso8CiB_Sk6VVt33AnUIu0bCx_8l7F_1DRc0SWH7V3MVCG4rOoEuAgDlY4t4eMoiFESVF9p_Vh6TK10uq8VB1ra6QTiLWnlzEuwLpApHNMNaOYp0KoyULKpPZl5ddilVG_bTIbyk3XcHqs6Bu_wAPOi4sZ6VTxu3RYtC_C6jm4ggAgFrjgiOHJt875FNibYqzakcUIfgMfPVAeUljREVlnE6_2jHUNA==",
      "snippet": "Colin Bentley (Head of Lending at Bridgit): A finance professional based in Australia who has been featured in industry publications like The Adviser discussing bridging finance."
    },
    {
      "title": "humantic.ai - Colin Bentley",
      "url": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHCXKKoT7Re8y27OroX_aLcMPQe7cnnIao9ejouk6WedrbCDjjkv5hU7jxtGczBUsyV1M28W0u7zxkttwMExK0KvLEhCYTe3yqWnGuru-gofim4JYkLUtXqKqeGl_bBjHC1ced1-iRvCtJNXDqorTvYAnuWBW1gqg==",
      "snippet": "Colin Bentley (VP of Growth at Intercom): An executive noted in professional profiles for his role in growth and leadership within the tech industry."
    },
    {
      "title": "goodreads.com - Colin Bentley",
      "url": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEQE827asoRmoXo2ww58l5j3tIH8RDesV38B4YyoGF7omJPm-fRpSZ1DG84peAcG3Aqf3eCGuMG7PsV0bA7UIew9cTHl6sgkkow77-4oIN5WiAzOkTcP1VvAQ2El6dxNIhhZjY=",
      "snippet": "Colin Bentley (Author): A well-known author specializing in project management, particularly regarding the PRINCE2 methodology."
    }
  ]
}

out_path = "/Users/fincent/.gemini/antigravity/scratch/aqs-scorer/discovered_links.json"
os.makedirs(os.path.dirname(out_path), exist_ok=True)
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(discovered_links, f, indent=2, ensure_ascii=False)
print("File successfully written.")
