(function(){const s=document.createElement("link").relList;if(s&&s.supports&&s.supports("modulepreload"))return;for(const e of document.querySelectorAll('link[rel="modulepreload"]'))n(e);new MutationObserver(e=>{for(const t of e)if(t.type==="childList")for(const o of t.addedNodes)o.tagName==="LINK"&&o.rel==="modulepreload"&&n(o)}).observe(document,{childList:!0,subtree:!0});function r(e){const t={};return e.integrity&&(t.integrity=e.integrity),e.referrerPolicy&&(t.referrerPolicy=e.referrerPolicy),e.crossOrigin==="use-credentials"?t.credentials="include":e.crossOrigin==="anonymous"?t.credentials="omit":t.credentials="same-origin",t}function n(e){if(e.ep)return;e.ep=!0;const t=r(e);fetch(e.href,t)}})();const E="data:image/png;base64,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",i=3,c="FeedbackAI",p="A tool to help educators grade assignments in Canvas.",A="1.0.0",a={page:"src/pages/options/index.html",open_in_tab:!0},d={service_worker:"src/pages/background/index.ts",type:"module"},f={default_popup:"src/pages/popup/index.html",default_icon:{48:"images/icon48.png"}},g={128:"images/icon128.png"},u=["storage","alarms"],m=[{matches:["https://*/courses/*/assignments/*"],js:["src/pages/content/assignments/index.tsx"]}],v={extension_pages:"script-src 'self'; object-src 'self';"},I={manifest_version:i,name:c,description:p,version:A,options_ui:a,background:d,action:f,icons:g,permissions:u,content_scripts:m,content_security_policy:v};export{E as I,I as m};