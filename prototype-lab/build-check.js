const fs=require('fs'); for (const f of ['index.html','src/app.js','src/styles.css']) { if(!fs.existsSync(f)) throw Error(f+' missing') } console.log('Prototype static build check passed')
