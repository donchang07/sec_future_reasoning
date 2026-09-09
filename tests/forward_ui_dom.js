// DOM unit harness only: no browser, computer interaction or network.
const fs=require('fs'),vm=require('vm'),assert=require('assert');
class Element{
 constructor(tag='div'){this.tag=tag;this.children=[];this.dataset={};this.textContent='';this.value='';this.hidden=false;this.classList={toggle(){}};}
 append(e){this.children.push(e);if(this.tag==='select'&&!this.value)this.value=e.value;}
 replaceChildren(){this.children=[];if(this.tag==='select')this.value='';}
 addEventListener(){}
 get options(){return this.children;} get rows(){return this.children;}
}
const elements=new Map();
const document={createElement:tag=>new Element(tag),getElementById:id=>{
 if(!elements.has(id)){const e=new Element(id==='runs'?'select':'div');if(['forecasts','ledger','metrics'].includes(id))e.tBodies=[new Element('tbody')];elements.set(id,e);}return elements.get(id);
}};
const system=JSON.parse(fs.readFileSync('docs/03-analysis/live-forward-v2.sealed-journal.json','utf8')).snapshot;
const record={system,kind:'imported',baseline_journal_sha256:'test',shadow:{positioning:{rows:[]},event:null}};
const empty={n:0,brier:null,directional_accuracy:null,actions:{false_entry:0,missed_entry:0,false_sell:0,missed_sell:0}};
const data={runs:[{...system,cutoff:system.data_cutoff,kind:'imported'}],logs:[],evaluation:{review_gate:{distinct_cases:1,review_minimum_met:false},pending_outcomes:4,system:{'1w':empty,'1m':empty,'1y':empty},human:{'1w':empty,'1m':empty,'1y':empty},human_records:[],shadow_comparison:{}}};
const context=vm.createContext({document,fetch:async url=>({ok:true,json:async()=>url==='/api/state'?data:record}),console});
vm.runInContext(fs.readFileSync('forward_ops/static/app.js','utf8'),context);
setImmediate(()=>setImmediate(()=>{
 assert.equal(elements.get('error').hidden,true,elements.get('error').textContent);
 assert.equal(elements.get('forecasts').tBodies[0].rows.length,3);
 assert.equal(elements.get('ledger').tBodies[0].rows.length,12);
 assert(elements.get('feedback').textContent.includes('40.80%'));
 vm.runInContext('detail(record.system.horizons[2])',context);
 assert.equal(elements.get('ledger').tBodies[0].rows.length,1);
 assert(elements.get('eligibility').textContent.includes('coverage:memory'));
 assert(elements.get('shadow').textContent.includes('0개'));
 console.log('DOM unit: initial render, three horizons, ledger, withheld drilldown, empty shadow passed');
}));
