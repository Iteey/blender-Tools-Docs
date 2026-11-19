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

// Deep-link controls. Clicking on a copy button copies an absolute Pages URL,
// including the current language, check slug, and optional section hash.
const feedback=document.querySelector('.copy-feedback');
const lang=document.body.dataset.language||'en';
const copyText=lang==='ru'?'Ссылка скопирована':'Link copied';
const copyFail=lang==='ru'?'Скопируй адрес из строки браузера':'Copy the URL from your address bar';
async function copyWithFallback(value){
 if(navigator.clipboard&&window.isSecureContext){try{await navigator.clipboard.writeText(value);return true}catch(e){}}
 const area=document.createElement('textarea');area.value=value;area.setAttribute('readonly','');area.style.cssText='position:fixed;left:-9999px;top:0;opacity:0';document.body.appendChild(area);area.select();
 let result=false;try{result=document.execCommand('copy')}catch(e){}area.remove();return result;
}
document.querySelectorAll('[data-copy-hash]').forEach(btn=>{
 btn.addEventListener('click',async()=>{
  const hash=btn.dataset.copyHash||'';
  const url=new URL(window.location.href);url.hash=hash;
  const ok=await copyWithFallback(url.href);
  if(feedback)feedback.textContent=ok?copyText:copyFail;
 });
});
// The #fix URL, unlike a plain check link, scrolls straight to the repair steps.
})();
