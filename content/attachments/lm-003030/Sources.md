# Sources — Anima Dataset Ingestion v0.1

Primary/current sources consulted before writing this spec:

- Anima Style Gallery: https://anima.mooshieblob.com/
- ThetaCursed / Anima-Style-Explorer: https://github.com/ThetaCursed/Anima-Style-Explorer
- Anima Style Explorer About: https://thetacursed.github.io/Anima-Style-Explorer/about.html
- MooshieUI: https://github.com/Mooshieblob1/MooshieUI
- nregret / Comfyui-Anima-Tools: https://github.com/nregret/Comfyui-Anima-Tools
- Illustrious / NoobAI Style Explorer: https://github.com/ThetaCursed/Illustrious-NoobAI-Style-Explorer

Verified source facts used by this spec:

- Anima Style Explorer is designed as a visual database for 40,000+ Danbooru-tagged artist styles.
- The explorer describes standardized preview generation with a fixed control prompt.
- It exposes approximate training image count / Works and uniqueness-related sorting/metadata.
- The repository also publishes a 59k artist index snapshot.
- MooshieUI states its autocomplete is based on Danbooru + Anima tag databases (~140k tags) and its artist gallery uses GitHub/Cloudflare infrastructure.
- Comfyui-Anima-Tools documents a data.js containing 40,000+ artist records with CDN mappings and uniqueness data.
- Illustrious/NoobAI explorer provides a second model-family observation source for future cross-model joins.
