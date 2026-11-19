(()=>{
const html=document.documentElement;
const themeButton=document.getElementById('theme-button');
const savedTheme=(()=>{try{return localStorage.getItem('ue5-docs-theme')}catch(e){return null}})();
if(savedTheme==='light'||savedTheme==='dark')html.dataset.theme=savedTheme;
else html.dataset.theme='dark';
function toggleTheme(){const next=html.dataset.theme==='light'?'dark':'light';html.dataset.theme=next;try{localStorage.setItem('ue5-docs-theme',next)}catch(e){}}
themeButton?.addEventListener('click',toggleTheme);
const menuButton=document.getElementById('menu-button'), sidebar=document.getElementById('sidebar'), overlay=document.getElementById('overlay');
function closeMenu(){sidebar?.classList.remove('open');overlay?.classList.remove('visible')}
menuButton?.addEventListener('click',()=>{sidebar?.classList.toggle('open');overlay?.classList.toggle('visible')});
overlay?.addEventListener('click',closeMenu);
window.addEventListener('keydown',e=>{if(e.key==='Escape')closeMenu();if((e.ctrlKey||e.metaKey)&&e.key.toLowerCase()==='k'){e.preventDefault();document.getElementById('search')?.focus()}});
const input=document.getElementById('search'),noResults=document.getElementById('search-empty');
function normalize(s){return (s||'').toLocaleLowerCase().trim().normalize('NFKD')}
input?.addEventListener('input',()=>{
 const q=normalize(input.value);let hits=0;
 for(const group of document.querySelectorAll('.nav-category')){
  let groupHits=0;const heading=group.querySelector('.nav-heading');const groupMatch=normalize(heading?.textContent).includes(q);
  group.querySelectorAll('.nav-check').forEach(check=>{
   const match=!q||groupMatch||normalize(check.dataset.search||check.textContent).includes(q);
   check.classList.toggle('hidden',!match);if(match){hits++;groupHits++}
  });
  group.classList.toggle('hidden',!!q&&!groupHits);
 }
 if(noResults)noResults.hidden=!q||hits>0;
});
})();
