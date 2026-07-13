import json
import os

path = "/Users/fincent/.gemini/antigravity/scratch/aqs-scorer/raw_responses_temp_A.json"

batch1 = {
  '"Ajay Chankramath" site:linkedin.com/in': """Ajay Chankramath's LinkedIn profile can be found at:

**https://www.linkedin.com/in/chankramath**[1][2][3]

### About Ajay Chankramath
Ajay Chankramath is a seasoned technology leader with over three decades of experience in software engineering, platform strategy, and enterprise transformation[4][5][6]. His career includes senior leadership roles at prominent organizations such as **Brillio** (where he serves as CTO and Global Managing Director for Platform & Products), **Thoughtworks**, **Oracle**, **Broadridge**, and **Xilinx**[7][4][8][5].

He is the founder and CEO of **Platformetrics**, a firm focused on platform engineering advisory, consulting, and education[8][6][9]. Additionally, he is a recognized author and educator in the field, having co-authored the book ***Effective Platform Engineering*** (Manning)[8][6][3], among other works like *Platform Engineer's Handbook* and *Domain Driven Platform Engineering*[10][11]. His current research and professional focus center on agentic artificial intelligence (AI) in platform engineering, developer experience (DevEx), and cloud-native infrastructure[7][10][11].

Sources:
[1] [buzzsprout.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFQ9fsxZHUubb4Mq6OeHwpFiUxZF_a952NmB8LgbNCohPfkxYaRId2QO_PoKvaERRhCpOQxQYh1zpHlwCu96l_BVViyPUBXdp8VEAzYZgnjBbEWr4zPuVOijk2cF4ix0TQR366-vWYIJPl0qzDz831vn47pSaWGpysIaB38YeWsGRanR2h0OcVz8hnCNRsZtRQvQqVzooLnOOkbjbhVrfs=)
[2] [youtube.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHa-IWYENr-o20_YdbKqFzEyRNjCZPNMMyscEpQaN6FndifTb8d7LSW0wE_NHIkLMew7QG9f4r2fXWohYmOyVWTCLMmslFesHHLrsGo-g2F7Ee8_9TNjodhMrUZXYIYmqIJ)
[3] [youtube.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFiUxEi2-KyJYcO5KXF-LVUoIk6G4GM1O-Ie7JZ-FrdQ0VWa3qNqWyjGCUFW0pyhWQx_Yz-nyZI_5hUMzKZMBUCrxtZ6P2gRP2pw1nwAWPma7TfOr30KAdRV9vxJwSBLLfD)
[4] [teamtopologies.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG3Jp2hsynFhN3dxjM9ywImt4VbfnPp5bRiZbSS2AcertmGFaHWuS0b9wQbc_XqizcSiD7QjQL--Bv0tKQhAJzpIwAa_oOsnQbCuAkenGNTLDktc9Yrf63TdCZLR70UqOtUA1pJxhVk33s=)
[5] [teamtopologies.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG3Jp2hsynFhN3dxjM9ywImt4VbfnPp5bRiZbSS2AcertmGFaHWuS0b9wQbc_XqizcSiD7QjQL--Bv0tKQhAJzpIwAa_oOsnQbCuAkenGNTLDktc9Yrf63TdCZLR70UqOtUA1pJxhVk33s=)
[6] [sessionize.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFscyu3X853qDaSTyvHvN0fTJSEm3ps88Vyb0MNbC58j-BvRcPxp4fUc6k860vR3GJNmHZjeixAmBtrMusWR35_Eis21xzE5I-ySNL0Ic1NGLHaJ9CxMEdwwcKiKvC2)
[7] [platformengineering.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH12skEcNP-xA7h3yvZlLZqd0PXJ39UIBZHNnHZrxoiM68y9PJLJIyHyIMoqOBgMWx0-_hyJc15pDFXZ41JqrcQCHOzYvJEUF0yCWIyMQ7Oa4Xt9xtMC-AmDAQhMy3LkKKWj_LAjNZf5ZGBKKZiXw==)
[8] [effectiveplatformengineering.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGONWN9V0eZW5_liWENdrHGPRlANT5S7AVFLBVZwYczYPvmIeZRd83mnoXuSxUhm5XQSuceGJlGdqJzmFCrlzXeLw7xzN53AsiDVTSb3-YwGqqOlVmanZni44IwIl7log==)
[9] [maven.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHxEmBqBCHDbkD3gMjA3zdW7ZbBkxZQvM-cKBvsZhs3kJkHihEtrCtlMUsUaHmKz4rYBIdu7n75IxZWQnQqL_eZsCed5lMftgWX-f425VnW3r8uqoQiz51o8nsKUifM-Oa6l3kBVBvSGRD-QXMEJlAKkNSwD0c=)
[10] [platformengineering.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFYWBEuvQ92wvDRjf7QbP_fU4pE-OGKI9f5AiMFoQ_dXlFE1Le9tenB6GlAJlFSOfOtKkbbsX1-ZFL02vrK30TGy7gYnDTBtc1nkkXOMddRaZegs22hGhzhF5HIqQZLqT0q8WLsSU7Vh2IIqnJox6IKSuhdRrZG9E5b38HFjoShOmjjrP5Ycdik_aqlAZ4ajIcnyKF_czHTtAVsKi0yUz8=)
[11] [platformengineering.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH12skEcNP-xA7h3yvZlLZqd0PXJ39UIBZHNnHZrxoiM68y9PJLJIyHyIMoqOBgMWx0-_hyJc15pDFXZ41JqrcQCHOzYvJEUF0yCWIyMQ7Oa4Xt9xtMC-AmDAQhMy3LkKKWj_LAjNZf5ZGBKKZiXw==)""",

  '"Ajay Chankramath" site:github.com OR site:udemy.com/user OR site:medium.com': """Ajay Chankramath is a software professional, author, and the Founder and CEO of Platformetrics, with a focus on platform engineering[1][2]. Below are the links to his presence on the requested platforms:

### **GitHub**
You can find his GitHub profile and repositories under the handle **@achankra**[1]:
*   **GitHub Profile:** [github.com/achankra](https://github.com/achankra)[1]
*   **Key Repositories:**
    *   [peh-course](https://github.com/achankra/peh-course): Companion repository for the Platform Engineering Handbook course[1][3].
    *   [platform-roi](https://github.com/achankra/platform-roi): Code for the Platformetrics Platform ROI model[1][4].
    *   [agentic-pe-oreilly](https://github.com/achankra/agentic-pe-oreilly): Materials for his O'Reilly cohort on Agentic AI in Platform Engineering[1][5].
    *   [peh](https://github.com/achankra/peh): Companion code for the *Packt Platform Engineer's Handbook*[6][3].

### **Medium**
Ajay Chankramath has been featured in several articles and interviews on Medium, often discussing platform engineering, SRE, and Generative AI[7][2][8]:
*   [Deep Engineering #19: Sean Alvarez & Ajay Chankramath on Platform vs. SRE](https://medium.com/p/e8a4a7536d4f)[7]
*   [Generative AI as the Platform Amplifier for Improving DevEx](https://medium.com/p/5a0c889f074d) (published via Manning Publications)[2]

*Note: No specific profile page was found for him directly on `udemy.com/user`.*

Sources:
[1] [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGIM_93TxkyEsmikHUBYJaruWV4GN0SNoyKCXhDjIznT5bH4mS2PvbZ1YfpH-EBkpbcy_aMWV8NsWLXBLTKu7x2BJYQvFROwRptXzelmgRxS0U=)
[2] [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGBPjdHRmzz7PzVkw7VHENJK3AMln6hWDF96t9sY0aUyAPVuvzFcu_HdQUpjdMRRyJIIYyy1m7igZN3MRL6w4diKurVvDDjeMO20b54ks8flVBVsnH1Rb0i33ko6pn3V-GiUY8rDNtrLnMF06WeN_VrQ9AUajvjhx7-BMoo3dvqSgwsMKM2gfMJqx-OkA5W7Yx-DlAWTGOhTg3JqpxzJg==)
[3] [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGIM_93TxkyEsmikHUBYJaruWV4GN0SNoyKCXhDjIznT5bH4mS2PvbZ1YfpH-EBkpbcy_aMWV8NsWLXBLTKu7x2BJYQvFROwRptXzelmgRxS0U=)
[4] [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEBvJ28FWqv1z-uEnJrjmFvufXXO3GhBs1u1LPnYfbrqUMP_Qi32o9P4CIugfDmnlMI2_iWtpGnHqjaFelAxMZthdRayf4Wm7IPb2JksUbU9g5z0GcLBkjnU-dEsOPn3mcXgmz6LC4d_iXdNEW6i1LueLp9)
[5] [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFeTpaAnzdkpAWZYroFEMnNTQwv6N1wuHXrBt8yM7fixWamRf5vmHaZiTMBO02y1Yv0k7LZGo5BdoijHc6j0QSboTJSqh0OcWlOjq5cn2f0futayGCG4tUfciHTqjZg0A_1F7D4eehu4tKJfBLQK5vvgWPebQqnnA==)
[6] [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEPfO4RXN5iGhBuH6uNwAt1RDxHKpruG9ZfT70-hCkg2zARwzV3Z7BbcUNxx4mYjyq-B21Al04C9X6ak3J2XdIXtYVXmpINGiB96wbs0oy-kVDYE-EG)
[7] [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGpDUn39v1DNkvDXJAudJ4Arywo3I7ADXOqlLvnp7gH3IaeaEQ2DZavK12AGpOX0oYn5dUsBkk-bn4zqc9kLyH2-FSZiC7oxc6l1a_s7g9nesjAM7Oai_eAUrBoROYt3D2L2ljjQJrWRsgZWUxPheJY8inDZ3rs5HPkjpd8V_yQtJZ3Mqd4N6YEfVYQH8jUbEEd1Auz23_pIBbmEKx4YcDiAyylSmRqkA==)
[8] [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGpDUn39v1DNkvDXJAudJ4Arywo3I7ADXOqlLvnp7gH3IaeaEQ2DZavK12AGpOX0oYn5dUsBkk-bn4zqc9kLyH2-FSZiC7oxc6l1a_s7g9nesjAM7Oai_eAUrBoROYt3D2L2ljjQJrWRsgZWUxPheJY8inDZ3rs5HPkjpd8V_yQtJZ3Mqd4N6YEfVYQH8jUbEEd1Auz23_pIBbmEKx4YcDiAyylSmRqkA==)""",

  '"Gabriel Baptista" site:linkedin.com/in': "No results found for site:linkedin.com/in \"Gabriel Baptista\"",

  '"Gabriel Baptista" site:github.com OR site:udemy.com/user OR site:medium.com': """Gabriel Baptista is a software engineer, architect, and author with a strong presence on platforms like GitHub and Medium.

### **GitHub**
*   **Gabriel Baptista Cerqueira (gbcbaptista):** An AI Full-stack Software Engineer focused on MLOps and scalable AI architectures[1].
*   **Gabriel Baptista (gobstech):** Listed as an undergraduate computer engineering student[2].
*   **Book Repositories:** Gabriel Baptista is a co-author of several books published by Packt on software architecture (e.g., *Software Architecture with .NET 10 and C#*, *Software Architecture with C# 12 and .NET 8*), and his work is featured in official Packt Publishing repositories on GitHub[3][4][5].
*   **Other Projects:** He has repositories related to web development, such as MEAN stack applications[6].

### **Medium**
*   **Articles & Mentions:** He writes on Medium, with recent content including topics like "When the Casino Closes, Will You Still Know How to Play?"[7] and professional discussions regarding software architecture, DevOps, and resilience in engineering (often featured in technical publications like *Deep Engineering*)[8][9].

### **Professional Background**
Gabriel is recognized as an Azure Platform-as-a-Service (PaaS) specialist, a university instructor in computer engineering, and an advisor/mentor for tech startups[8][3][9].

Sources:
[1] [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGcbRHVBdvX_ajBN6J03XJfTIlg5FYei-sl22WvPePeglE77F9ZJ-c_kZrJ5-XuBZoFqwhIKtRgfowZBcHT4m-be5HxkKVc0rY67uEtMLxWdg4D84o=)
[2] [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHe9A3LzDog-Pus3KYpzAg36ybxC-wtPvqJzkpXDWL-4VsDYdaiBu1ouHJ5Eb0mQOK83bM7_0qLXs792R00kO1ZRrbnYKLoWfJxKFpMDB73aSc=)
[3] [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEUoK2woXxDHuIaOwzKG4Ezm-KDQhFuK0ICBUjV8FxycXQ9VbpXlr9EVfAYSYvSJHYtsWP8BAciSlJzExPnRK_B213Jzl2OlLqdjSSOzOnWnGqnoZNxIZINj395h2Q9MCHfccY7C7OskYdwIcIjl_2Yvm4CLX9nFCy7ILoPjeXZCEaq02JE76ILpPx67A==)
[4] [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGKEkK3RCeQgzEZxCZ9Qg3MrLulgMQDhsPJTFTGdsdotZiJbSPZsa3p1yCTqQSo2dU-fiIPN-xxNFamYxwyDGBlru2yPe8oYnceko_CJXPBDGlQOkgSL53f1eJIiKdSyRy3sAufv2YikyWS2bQff7NaJmY3FoMgYYPOTaauCNZcxOFal23q)
[5] [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHOg4fw_5HPbt0kybfSi1M-tsuoiY19jM2V6psGf1x1hQD9tN-hZDOPmeid4u0ih-DY0Go6LW81l_m4WNBhU1HnNsaHhtdWu3K4gIxldhEOLl6P_438k1mbKoUqZ-srMiZL4l9cEbXZDSLEH1V-gzoXr9MuL529_AUSOso_ipY3ZE1vVad-DU6lWmA=)
[6] [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGXqBSAHNfnbCOkjA8Gb5SDwOJgUu3qQdWdVQx_j_oDxMKrTibLGRDGylC8fs3ra2os8LlAk_WXkdMozaJ6sYtHaDIXzcikROz7pvkPU4z6f0IgYSfNfvZmrXok5YPkZrOQxiir2TVP2pBZLQ==)
[7] [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF1mDYVHhDEdEZqgjFMBMKT9AKDQAibsVLDrTEMgFKbEWVI2-_pE3v7QoA4VR-VBE_ULGOYdoyAYzAmwGD4dAKjxvo3sNqJqiSq0SY8c2axfxQ8sGepVoK_1XCz6PWSm2-WQlWfl26NKC5ZxIN22s80tue5EA7vmhb2FWTEL_nnageeDRCWOQxaBBO10O3Qcv-pIlkYsEjogLnmw2Q=)
[8] [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEjxDIWcCHNwGcYwXMulqaw7kp4qsUCUImoTIjT2r7AZUd146DgKT6N7aAiXGnVYW2EwTE68pcVzZVB2xKG7y59xUCJGai-VsI3otTTIv8d-8y0B7pC-tLwhNQV537lx6ijd8vJTSGqNRM6QB5axi5-miPtwdalvbZbPGHcbjCH8XB87zA_0nVeSaDGBPyHoxnOkC5ywemrzsQY8m7oUUPk0lHpArqy4zObMbjQsgLU9Mzzsn8N42MdO46Uu903jUvK4wEx)
[9] [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGkhcyuuz_rv5KqB3GlBZ58B_20eDq9DFydgfy3WytUlQxzPLVf56Dsr6Q_dhkp_wpXrT8SOgmylRHdiAkswAHpEI4rYheMnyYJ9qVSqGTTkhV-K89pcdxypW6CUaQp1XUK7jVZRzsyh4zMpPnJHtwQkovEr5XLD8yhRdDmUvBgvlVrYkhjiquqLc0PxFW8jim_BGUxJb8t)""",

  '"Francesco Abbruzzese" site:linkedin.com/in': """There is no single, definitive LinkedIn profile public for a "Francesco Abbruzzese" that consistently appears in search results.

Because "Francesco Abbruzzese" is a common name, search results often point to different individuals, including:

*   **Software Architect & Author:** A prominent Francesco Abbruzzese is a software expert and author of books such as *Software Architecture with C# 12 and .NET 8*[1][2]. He is known for his work with the Microsoft web stack, Azure, and as the creator of the Blazor and MVC Controls Toolkits[3][4][2].
*   **Other Individuals:** There are multiple other people with this name, including athletes (soccer players)[5][6], individuals mentioned in news reports[7][8], and other professionals[9][10].

If you are looking for a specific professional, it may be helpful to search on LinkedIn directly using additional filters such as their **location**, **company**, or **industry** to identify the correct profile.

Sources:
[1] [bookswagon.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEv13xeTWH2A0kg_APYeM-Q1E9HM78idezaJCEdqi9QVW49Cin5elm9HJryT8EFGR203jjKUWbqtEJyRW0VSZcliR4V6aDGNdTDi8xn9hY8I_EfVHqM2m90MW7LFa7uaX5Plb_8Y_iKi1rC2LAA5cVrh3f_oYX--VLDwtWwI1BupQ7n)
[2] [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHuq22VwLq8_iLUN6mOJ0cKuaTnCi2he-RrcKyif81aYpz3KgHKJP-YSzT5jwAzRozWA-nVpC9j4pW79ibOgLX4N-CBmrCepv8Mmo7kCIz-N5DNO3EXMA5n7RmOs7_E6qZJeyYDfW9LEc_uHmOmsLwjCvOwQGLSOdaRVynv1FUWx4M6HFcnVtkuoHSTy3-FKaxS7MPndEpT_wt1OCuVXZsjkKXxhWLhhjJhFLlHaBNhYhXgCfZHdxFHYn4P5DsqhjNr5qa0)
[3] [packtpub.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHOZO_-NhAc62taAku--9rGnZuZgOyPLf8IL1GVV9u-mg1_c3lUTijh5JiiAnTe0gntZbqmCwO75Vmmynti5moZNjK0_53hpgxjZEgObreGZRSdsq2gdgVCWiMvOuzXIalbb9Cz-iew906V42XXh8hufFhUScqCbgw66dZLhrNG3YTkaLOoDdKq56tuTKyQb589SfevRwviMuAX9RHM3O38cQNZNX0flSFcxQod8dSHssD3B2lYOSpYdmrnTk4FMvAiUrwwmEqWRQ==)
[4] [sessionize.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQElB5eR4BzPIz59OMfpokkyFv3yQs7PXSjY_rq1Y0Q87HxauCwMWfzV2wGE_FmbkBUj8CjKS-X6kRLULPYT0woHq4GRGWF0faBZfMHt6h5KwIZZh6L3VptTnF0A-WB4_yDngg==)
[5] [transfermarkt.co.in](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGmcn5xwrwQ7fWmRtTjapbFLlXjwNLXGsv9fyAIQHRdJ11RVkXqyDP5fiSvxLMor_yTJkrJZvaE9TvD1VM0jHBrSnSDLp62_uPflkw2G-oUrCTM_SYPRWNKhmr0UjRD0oNf54h_M70YmMKiYDDkjN8E3ozQ5ciu3sqZPTQCiFux4lY3wrHui1tnl-Lm7UbvGa4=)
[6] [transfermarkt.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEl8eHQRmxGIFGUgzdVoxf-vaWi9FpafxhBJh14FkzkhIj3WlPA1NgVPJPN9zwW3dD5jF1ZDzDusSzdZql_E6KWfXf6MTp6Mu2vN6jpanTwlgbczuhmKbdRXmJD7VFi0NgtMR_b1VnOOi-JIBCNkw10ysD6pnXp9KDwY6MCcNE=)
[7] [lagazzettadelmezzogiorno.it](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHj9kokZgacTx0n56jtjqbDg3tIvX0t8eLC0QlWhtE3rASXHiIctGCgDMiNDVAfwaPTx7TKGljcmJPdGMKolUBJFwq1b1Y00LCPhZ5RePDRT_rpjK1sKo0u8xKA7nY7GT5Zl2RsL6xKgWhDvkvfMQJJDLJlIbJv9rw4q3nGifEEI42W82mPv7pGhWqb4S0latLzgKeFMr1kFDDKBh87go2b7deb2wd73Ry-mDTY481CBjm4ldwGdSjWJ-VvC84JxrCyzAPqTbxQgWuhNY27zpAUqZq-Z_yrP3vMR1yVkGTn_560AOswPWrCrcs6ySk0xVRTRfI6wP8=)
[8] [ecoaltomolise.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHISKCLrhSqHm3CgyrmJnEZ7veTCdu5HOS-xUCsP1au8QbEkRGRqEbMybIpP4a7D4BkD483WvmoOZIlMXDOjPrkj3-tKLOzaFy4XTiE9bKK8Gzci8D_vQBlXkMfcPy4phEj7rixw3lECwbDWZbqO1kc_mOY3qZCpcWSshiPLJ_RzBywSUsNQurYs3Brbb3OL9VJF8XpRf7gNqbpEgBdujRJRg==)
[9] [prepbaseballreport.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHvhC_LwjOIV2seQxFmMD_9ie4R109vNIpZiu4VQoraHRXxpom_EqhLh6W9jMUrIcSC9kIdKmeP_TJo1Pex3bJG1d8aPYb3h5Bpoyanu45HbBVIG0c3E4n_HP0kyQt8SrSd9gStpe-W5fMv-rTS0uHAni22FHO4i-Ml)
[10] [quora.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHhyirYqWonMPwL42RDA8dY-vHB4Rjl2SdddYzfCiyO7qYh51pWnqKnSHBmxdbexVePJ86benRE7RD-nuPKhsyEe1SKLyVOBY2mGwmvzv5UiTezEdKgSc1RYuhYaRK4C6pRcjtNUIrD)""",

  '"Francesco Abbruzzese" site:github.com OR site:udemy.com/user OR site:medium.com': """Francesco Abbruzzese is a software architect, author, and developer known for his contributions to the Microsoft web stack[1][2].

### GitHub Presence
*   **Profile:** [frankabbruzzese](https://github.com/frankabbruzzese)[1][3]
*   **Key Contributions:** He is the founder of the **Mvcct Team** and the author of the **MVC Controls Toolkit** and **Blazor Controls Toolkit** libraries[1][4]. His GitHub repositories typically host code related to these toolkits and supporting core components[1].
*   **Book Repositories:** He has collaborated on multiple technical books published by Packt, with associated repositories on GitHub for projects such as *Software Architecture with C# and .NET* (various editions, including .NET 8 and .NET 10) and *Hands-On TypeScript for C# and .NET Core Developers*[2][4][5][6].

### Medium Presence
Francesco Abbruzzese is frequently featured on Medium, primarily in articles discussing software architecture, DevOps, and his co-authored books[7][8][9]:
*   **Interviews & Features:** He has been interviewed regarding his expertise in resilient software architecture and the role of DevOps in modern engineering[7][10][11].
*   **Book Reviews & Excerpts:** Several articles review his books on software architecture, and some provide excerpts from his work, such as chapters on DevOps principles and CI/CD[8][9].
*   **Community Interaction:** He is also active in responding to technical discussions on the platform[12].

### Udemy
No direct user profile for Francesco Abbruzzese was found on `udemy.com/user`. While he is an author and instructor who teaches at universities and mentors startups, his primary educational presence is currently linked to his books, blog, and technical tools rather than a specific Udemy instructor page[1][4][8].

Sources:
[1] [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGUqm1haORA0bqb89fxrAdTbaZx-9vNMG1oO_diHHK8ZtND4s1vk5H3ZpWtd8MzZhffQCmAVAV8LI9I9JuADgdQvAyuodGLSWl0yBndoFARFxa-o3yQVb-i)
[2] [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEmPGqZbZPG5VDqq2bJ_ya0F0yVdC3zDmxIVrAGTtRdhfCtcRKZdLn8ripUJ1msF2AJYs4jLyJGnW83B98xpZM75UT6zDGV1DEybx0MnJuXrSznffoeUdnWjAvH9jSkKQya5ctPa7XVoKuYfd240OlSbOhyZQV36M5dWw6lKut28OGzG1klvqcZrgU88zGEis0=)
[3] [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGUqm1haORA0bqb89fxrAdTbaZx-9vNMG1oO_diHHK8ZtND4s1vk5H3ZpWtd8MzZhffQCmAVAV8LI9I9JuADgdQvAyuodGLSWl0yBndoFARFxa-o3yQVb-i)
[4] [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEM2QlPXdYtMZJUMQqPzwLQGHHO16S6Jab99uKArBDItsfMlo9cGM06QFFIgwoJDF2JQPqbqjWgbI80A3xnimxBbnhR5ustyTsRqBsx9i6eiz1jGRKtfbXNYp9Xm3XKhpwNsrB_2dnoXaHItkrX7De-zj8pep625DD1nqU2GJ-JtQmHyNDeB1PEYPbx3A==)
[5] [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEXBrTsJdGMo3kav5vWBPwl_jq2dCh9m0RhpmMUqvTYfR4jl3X03Ny9fg3rqZrj83Yl4k1FQHiHfTTicfmxSLC0jP00nRWEwWbZneRqqD0pluNQRzqbbl7V0F8FWGB8VKUNZiy3m1PsqT95kmZyOPsIRWIVixS3RvnHhTMXexQwiDld4Cc4rbIWeZI=)
[6] [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFv3Tdoe6oXYh_4GI3QHxI40jtKVYNWOUpItLIqR6rX39_wLUnJiq6edZA4kYSmpf0MlqXAoU5tR7SYlbEnamneo3rscUwx-rM0omCMu-OSi_rSEfVn8G0FemtWmVzDkmR9MnO2mgB6nKoRTXGERIvY-F4QSHL5nvJNwWjDriL0cYFscZxx)
[7] [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHWbwGpUjwrhO-E9UjctxMMCFQRZnCNBpIoV4p4rgBjk5MqJgsoix84f-AACrFJQeiv-m8VNrnJ-dgqkXuxN1AaUA1Cgp3CF8zBLcp_JwYPddao-Dzxb_HKL6TLRBHcvO7qHys2iVYSdFNZuHwUainzSKPSZQpUsojINgLqV8E7w1ZmhGsyXkVN8WwZCOCELyXlpGEJMWPPX83352BMHPob8YuxjmxkxI8CVKPZFzLWIO-umecP5aNshEQiP5PkHj3OxV2o)
[8] [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFsPimsf-mtb7yBE6VetGvNSy4Wu9q-gcaGZmfWGTlQdftrvmh85PAWWJ7ZnkfhMB5X4xCdvFHkingRd3EYc7tI18t6zUBEW82Y58Gi1fIN9dc3-B8O-gEbv0FI6wEpewJZ8qsAgu6P_Pnaanz3jueq-cdNT2BoCJy5-H8b4PzGpdzmlGBlzs4G65zZivIFjLhRk8fhnzDd)
[9] [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHWbwGpUjwrhO-E9UjctxMMCFQRZnCNBpIoV4p4rgBjk5MqJgsoix84f-AACrFJQeiv-m8VNrnJ-dgqkXuxN1AaUA1Cgp3CF8zBLcp_JwYPddao-Dzxb_HKL6TLRBHcvO7qHys2iVYSdFNZuHwUainzSKPSZQpUsojINgLqV8E7w1ZmhGsyXkVN8WwZCOCELyXlpGEJMWPPX83352BMHPob8YuxjmxkxI8CVKPZFzLWIO-umecP5aNshEQiP5PkHj3OxV2o)
[10] [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHWbwGpUjwrhO-E9UjctxMMCFQRZnCNBpIoV4p4rgBjk5MqJgsoix84f-AACrFJQeiv-m8VNrnJ-dgqkXuxN1AaUA1Cgp3CF8zBLcp_JwYPddao-Dzxb_HKL6TLRBHcvO7qHys2iVYSdFNZuHwUainzSKPSZQpUsojINgLqV8E7w1ZmhGsyXkVN8WwZCOCELyXlpGEJMWPPX83352BMHPob8YuxjmxkxI8CVKPZFzLWIO-umecP5aNshEQiP5PkHj3OxV2o)
[11] [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHWbwGpUjwrhO-E9UjctxMMCFQRZnCNBpIoV4p4rgBjk5MqJgsoix84f-AACrFJQeiv-m8VNrnJ-dgqkXuxN1AaUA1Cgp3CF8zBLcp_JwYPddao-Dzxb_HKL6TLRBHcvO7qHys2iVYSdFNZuHwUainzSKPSZQpUsojINgLqV8E7w1ZmhGsyXkVN8WwZCOCELyXlpGEJMWPPX83352BMHPob8YuxjmxkxI8CVKPZFzLWIO-umecP5aNshEQiP5PkHj3OxV2o)
[12] [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEnyf3qS67h80RF3kVpW-KTKT_XRDb13VNDlAiR_ad3P7geWXH6kZT1kw5MV4c2_ogymshQWTGyzQOn37NfvcvPNVinAxhkCUYiHIuOZj7j1Sjdo218YHzVF4KBHdfPGoPRmpT2LhdRsfbN8dD03LCu73gJzgRH2J0TPk3chipQBEigw2j2XYAfjqgKIyBQq5KQ0TEpz_KDVH3ihPx-Fb3155B_)""",

  '"Mark J. Price" site:linkedin.com/in': """The LinkedIn profile for **Mark J. Price**, the well-known author of C# and .NET programming books, can be found at:

**[linkedin.com/in/markjamesprice/](https://www.linkedin.com/in/markjamesprice/)**[1]

### About Mark J. Price
Mark J. Price is a recognized author, programmer, and teacher specializing in C# and .NET development[1][2]. Key details about his professional background include:

*   **Author:** He is the best-selling author of several books on modern cross-platform development with C# and .NET, published by Packt Publishing (e.g., *C# and .NET Modern Cross-Platform Development* series)[1][3].
*   **Expertise:** He is a former Microsoft Certified Trainer (MCT) and holds certifications such as Microsoft Specialist: Programming in C# and Architecting Microsoft Azure Solutions[4][2].
*   **Experience:** With over 20 years of experience in education and programming, he has authored official courseware for Microsoft and has helped many developers prepare for Microsoft programming exams[4][2].

Sources:
[1] [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH0Hjnee2yBkXSF07YzfRKhxgAUCISeB8U5gpD0ekZfYjB9WPPEmZFNJuk5OIqL0UVEpYtweYf-0_ZWETBqUCO-9lqBqJyyJYFzW1I9FlGfbxWVPQ==)
[2] [packtpub.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGFVPbcf-S719KFSQbUUnZylbneEzvDJBz_UuEGZ0y9zbkieKkJh6SrTTabWXqAsYmpqxF5ZxcwhPcJJcfMQm-TQ1xxF-aShEPmp2G86b5JCXdDuqbqqy2_XpJN5edfgXx4uOJKTeRpVS3ONkIExQfibQzZepE=)
[3] [azurewebsites.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE3wGqanEEtSqt3hTyBZ9_sf7eYtHRAWT5ksdt9RJaQlzaQ0PcrFVO7qT45uOSjKjI8-62agBj4hM9o7esIpp2wc2-XW64wNfu8SQiRSqxN5akI6wAXla5LfqI=)
[4] [goodreads.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHNV8oYZNiJQKpB-aetoUwI158Zt7d62uQKwJOV5Yt7tiGbhIToH50HBto4U6giHNgttIUX0NPzfbZLHYCK0wJKMpBI2JCRKs4iBVElf3WA1VDRUD7vXm8Ea942VczRFg2IpSAEuVCYucHCQQgDdqOJ9w==)""",

  '"Mark J. Price" site:github.com OR site:udemy.com/user OR site:medium.com': """Mark J. Price is a well-known author, programmer, and teacher, particularly recognized for his extensive series of books on C# and .NET development published by Packt Publishing[1][2][3].

### GitHub
Mark J. Price maintains a GitHub account (`markjprice`) where he hosts code repositories for his various books[1][2]. These repositories provide source code and examples corresponding to his publications, such as:
*   **[markjprice/cs14net10](https://github.com/markjprice/cs14net10):** *C# 14 and .NET 10 - Modern Cross-Platform Development Fundamentals*[4]
*   **[markjprice/cs13net9](https://github.com/markjprice/cs13net9):** *C# 13 and .NET 9 - Modern Cross-Platform Development Fundamentals*[5]
*   **[markjprice/cs12dotnet8](https://github.com/markjprice/cs12dotnet8):** *C# 12 and .NET 8 - Modern Cross-Platform Development Fundamentals*[2]
*   He also maintains repositories for older editions, including C# 9/ .NET 5 and C# 8.0/ .NET Core 3.0[6][7].

### Medium
His work and books are frequently discussed and recommended in the .NET community on Medium[3][8][9]. Articles often highlight his guides as essential resources for:
*   **Beginners:** His books are commonly cited as top-tier resources for learning C# and .NET due to their structured approach and practical examples[3].
*   **Professional Development:** Many "resource list" articles include his titles (e.g., *C# and .NET Modern Cross-Platform Development* series) as standard reading for developers looking to master the .NET ecosystem[8][9].

Mark J. Price is a former Microsoft Certified Trainer (MCT) and holds certifications such as Microsoft Specialist: Programming in C# and Architecting Microsoft Azure Solutions[3].

Sources:
[1] [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGiSH2Hlf5AeMEeWxNMjIgafONfrzxT5wDm4q42tFZGZ3k_7n_4ygs0XPnRezOswymZJtdCaLteS58SXukjrC1xYOq5gNpPqxKNSYZ7DJTYKbyVmw==)
[2] [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFabVwbn03dsgfFD6N9nUdgMSuKFXEcyvoragMLFZFCHmWbdK-iTr-Z-t5DlBOTQrp-SK-2PphTuPxu2JTsVG_3rFK-LeRXUYr4I-8EXXG-8K92rhDzBjs_JTXtogQVLg==)
[3] [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEggLOi1JH04gcsmqcYPQFe7CKPVRSCF9ZoWH4tnk6Y2b0NAcsNWBo8pXZ-anPM8eoWNzwsc2yv_aL7EFfTAvvGO1DaNpRMtCrQb1_sBiscQapLkHhLTfTdA7w1GKzlkCEhVegqnaiDsgZBh-Jzh6SuiyQbqnZHYjk2iWMRZgnG0vI4fZoTILw=)
[4] [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYGkbp5fv1JwT0gTN3jMw2DiV_WnTPeshw-zLm-KRlxUZzAZICcV2uxdrjx46ZKUmXgqPjei3lCj4ZFyflcQEVHaegzmrGPtlPM9DEZnODqwa_us2FuUyPqNkHggXRa6)
[5] [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHNS6Q_wX6iMFVet2GieQGPh1GJcjy1UGUm685AG6ThW-SyZq-tQxVzlM2xXxfMUVn6y-DYbqjUQFc1w6ag6zOeMtTlIMAFC0LhCF64HasdBLGe09HoizNXtHxNMA==)
[6] [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH0Bykp2MHH9wuZXZ-r9IgzA2Qp2B8XZGuXwdENPCjuvsYd7KHZjf36eF2Yd5ypM1qQ2lPhqIuGdPyT7Yq7K4p_GjeOeCDDZMPqimGWy02wZREwWlt64FSCIVdhf-DW)
[7] [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGXEB3q2FCmf9ywMGJ4WYbrlDY57guApxJ5bK-B6HbXVY3KQfDdOdyRUuEVOaEoiW4Rb3MFbWExSMX3VZswYD9WYxM_qfCRpj_WanfxWYDWvaNW_MegbNC5LRwaCCkCGycRwQ==)
[8] [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQELfSo0YSEGbe6mGCMyB1tZoqStnRt89FnvVa4uvQjYzZQsh49BsE9f0PyT4IkA-KKGixX5WDFFh5HOzR4eIfxvygUDAbZFGaHwysFqEDp3RhzDx70VMlakowX_tNctygAV1ZabLn2mg9l29in7o3O4Fk4s-XXXQpZWxNUWJ_KAZp1kIGbxzF_R5LWZmleGe4j4MshtSalufnRm7DzMt3A46EG0_9cRO2dzfNN4ex6M0Qx6NJsiQdw=)
[9] [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEGlD90tfHQaxhN1Z6FcGucyCOjnjTdkt90deIl6EIuoGavOaZ-oLG5xjsmR9ycyw3JxNhYprQgr1xFMg3J80Sw-j6zvvlmBXUaIWkgiIhR87rHJhzcHURmY462g35EyKvdh_1Va7L_jVGXHV0aeCNeWlgauLi3NeON2lu_-LjAmx_9WDTRrID-84PRNS4n4NqaAgFOn_4s1Uy_)""",

  '"Toi B. Wright" site:linkedin.com/in': """Toi B. Wright (often referred to as Toi Wright) is a software developer, consultant, and author known for her expertise in .NET, C#, and Blazor[1][2].

She is a **Microsoft MVP** (Most Valuable Professional) in ASP/ASP.NET[2] and an **ASPInsider**[2]. Her professional background includes[2]:
*   **Education:** She holds a B.S. in Computer Science and Engineering from the Massachusetts Institute of Technology (MIT) and an MBA from Carnegie Mellon University[2].
*   **Author:** She has authored books on web development, most notably *Blazor WebAssembly by Example*, which provides a project-based approach to building web applications using .NET and C#[3][4][2].
*   **Community:** She has been active in the .NET community, including running the Dallas ASP.NET User Group[1].

While a direct public link to her LinkedIn profile did not appear in the search results, she has been widely cited in tech publications, podcasts (such as the Azure DevOps Podcast), and book repositories with references to her professional credentials and online presence[1][5][2].

Sources:
[1] [apple.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRJHoVohWnOsHImjJEL4XAkMvS8uVjlnR20Oirlqil5xoXXodmqHP-BjSPetow8cD4aMYZ5v25x24lIS1MZN5_rnxGfx-y4v0T9saRJvEi3m-vPMj0B792RtJb5D_cSgH6-aEVEa3TMev7wbveCoLsROtPIgvG_p8qymkKg6vZaa4ip5RzJBHhuMcf1RbmbgfBoNAKbCGDjZslgE9R6cQzgMOdvSH6eg==)
[2] [libsyn.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFqfl_aPYWz56W7l8CdMv3RrPr8PXcYdubPjGtnJ0iDNmJbAALFEuNJppZXGi8Dsd9ueeGD6_wWk0tH-f0GL6EwKAN450s6z3Dt3oK87bo3LjHpJ0ENE2vSlyzLD4rDPhkmOndMpMEASmndDJhtPq2Xpg==)
[3] [packtpub.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHO9EsgjXb6GBsoCLvBcOwHKitv4Rv8EU1COl_phJwqIDX7P7Av4ITHdLEisu3PKWkxkfkrydcseL0YW6ATZ6gEAjYd-CnBm1C6nqBblPydvvpAw1fgrtf9Yg4-QehNOw4Pg01qjsoSu_0rO1snyNxV2uv6IX2bmgPfSj1eGTzI5z8SeYkgDw==)
[4] [bookauthority.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGoRtklBIvwyWdtEhiXPwmflEJu1tqOeoiJjrhdPB2ivlMWIkp2hACsRLGB2vXX5qtClsePcilamkwPai_uTj5Q41qNL9ahqFzyByndQ_U0xeBs3nNVsyx4-HyC-xGKLWjgfSJ_WTweYIdkpY3rl_4EAyP9zw==)
[5] [youtube.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEauXDjyJHZcxbYMap717MamLQzwieErvV26KI6rlO1fsI45kzS5wcqzC1ROxvMMLTO3aWULvRwk_pkzBS_k7usMNHj04xZ8jfoeWTvaG8RGFb8IOIm6RDyC_fkiT43BYE=)""",

  '"Toi B. Wright" site:github.com OR site:udemy.com/user OR site:medium.com': """Toi B. Wright is a well-known author, speaker, and software developer specializing in ASP.NET[1][2]. She has been recognized as a Microsoft MVP in ASP.NET for over 20 years[2][3] and is an ASPInsider[4][5].

Her presence on the requested platforms is summarized below:

*   **GitHub:** Her name appears in several repositories associated with **Packt Publishing**, specifically as the author of the book ***Blazor WebAssembly by Example*** (with multiple editions, including the second and third editions)[1][2][3]. These repositories contain the code examples and project files for her books[4][6].
*   **Medium:** While she does not appear to have a personal account indexed as a primary author, her work is frequently cited and recommended in technical articles and .NET learning resources[7][8][9]. Writers often include her book, *Blazor WebAssembly by Example*, in lists of recommended resources for developers learning .NET and Blazor[7][8][9].
*   **Udemy:** There are no direct results for a Toi B. Wright user profile on Udemy.

Sources:
[1] [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE843XuZExkZRDbCoO7lEAZp-52A5VWPlsicPGjyJh9Css34TWvNhhA9UlOqj4kC3euLJNrKvlL2inIXZh8zYTopnAf6wg3YZYlThkts6b6Mbzk95qmBVOPl_5DrfSTQ6J1ORxMZ7svOg6brPMToXerSndcNX7k6lrlRyu_WRx6Gcy2j3KO)
[2] [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHY-_FpWCyjJzGy1Y2IMobIkvRLzG8OKJ6eHtrUzASdeplgk0py1BHOOh7CaWgpoi8ZI9n4DGds-dpP1HFipIU2iXFZNTfTcDHTolF9XqWjCcn6HRtpbqWWRfXxWX-KHkcgFvZZOYYvzqfAfuEo3MZ_sSshDL2J8Y-k0tfoOES6FqXEuMM=)
[3] [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHY-_FpWCyjJzGy1Y2IMobIkvRLzG8OKJ6eHtrUzASdeplgk0py1BHOOh7CaWgpoi8ZI9n4DGds-dpP1HFipIU2iXFZNTfTcDHTolF9XqWjCcn6HRtpbqWWRfXxWX-KHkcgFvZZOYYvzqfAfuEo3MZ_sSshDL2J8Y-k0tfoOES6FqXEuMM=)
[4] [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGEhZKAvafslMDPebP9WnGLcrpjMVKXxBq_k8p7mIl-akrLJJ9OjwN3ZQttOYoyIHqPbfx_mghwgSgesp_3JvkWP4zg9qh-TADi17H6EU-C5dAmyVpUCvpxKRd2CsO2YIwUxBJ4wGHk-8ACVLuIGuWuBa0AM3y4)
[5] [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGEhZKAvafslMDPebP9WnGLcrpjMVKXxBq_k8p7mIl-akrLJJ9OjwN3ZQttOYoyIHqPbfx_mghwgSgesp_3JvkWP4zg9qh-TADi17H6EU-C5dAmyVpUCvpxKRd2CsO2YIwUxBJ4wGHk-8ACVLuIGuWuBa0AM3y4)
[6] [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE843XuZExkZRDbCoO7lEAZp-52A5VWPlsicPGjyJh9Css34TWvNhhA9UlOqj4kC3euLJNrKvlL2inIXZh8zYTopnAf6wg3YZYlThkts6b6Mbzk95qmBVOPl_5DrfSTQ6J1ORxMZ7svOg6brPMToXerSndcNX7k6lrlRyu_WRx6Gcy2j3KO)
[7] [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGtTueM5Op4VSmzvrnRevKCXv5LWLdLbR9GRwkgpl2f--ACh5kQebxHG-Nc7ocO1n8bXDhzbm-MErLL5zAdU0DTHpAk4qCzTcDbzhpXHhF6L1vxBNkaCHm-zcrM1nDxG3gnFLE0NtvfF4eqAkoBHFJNIPfTX8jmvU4-9YBiLaziQQ45rqfZ)
[8] [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHNnaUjcVThcYrIFX8lDBUvQfbz66QwMF-Q7WnDzdJAcVvr0ECuXVOOj1SMqropBCqi-G1Ho3hcnKHc3Dt9dN6m3GjOmf_aqiqOHynd3i3XgwoQuOhyIZx5Ys1_uyJjZLGE0D-R36z5ywo3gNwZ6LqxCriob_t_cKtUdOC5OYrs1KCAD2f7PRzRczouqUGo_OQF9DPOXH90S4AG)
[9] [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGtTueM5Op4VSmzvrnRevKCXv5LWLdLbR9GRwkgpl2f--ACh5kQebxHG-Nc7ocO1n8bXDhzbm-MErLL5zAdU0DTHpAk4qCzTcDbzhpXHhF6L1vxBNkaCHm-zcrM1nDxG3gnFLE0NtvfF4eqAkoBHFJNIPfTX8jmvU4-9YBiLaziQQ45rqfZ)"""
}

with open(path, "w", encoding="utf-8") as f:
    json.dump(batch1, f, indent=2, ensure_ascii=False)

print("Batch 1 saved successfully!")
