(function(e){function t(t){for(var n,a,p=t[0],l=t[1],s=t[2],c=0,u=[];c<p.length;c++)a=p[c],Object.prototype.hasOwnProperty.call(i,a)&&i[a]&&u.push(i[a][0]),i[a]=0;for(n in l)Object.prototype.hasOwnProperty.call(l,n)&&(e[n]=l[n]);d&&d(t);while(u.length)u.shift()();return o.push.apply(o,s||[]),r()}function r(){for(var e,t=0;t<o.length;t++){for(var r=o[t],n=!0,p=1;p<r.length;p++){var l=r[p];0!==i[l]&&(n=!1)}n&&(o.splice(t--,1),e=a(a.s=r[0]))}return e}var n={},i={app:0},o=[];function a(t){if(n[t])return n[t].exports;var r=n[t]={i:t,l:!1,exports:{}};return e[t].call(r.exports,r,r.exports,a),r.l=!0,r.exports}a.m=e,a.c=n,a.d=function(e,t,r){a.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:r})},a.r=function(e){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},a.t=function(e,t){if(1&t&&(e=a(e)),8&t)return e;if(4&t&&"object"===typeof e&&e&&e.__esModule)return e;var r=Object.create(null);if(a.r(r),Object.defineProperty(r,"default",{enumerable:!0,value:e}),2&t&&"string"!=typeof e)for(var n in e)a.d(r,n,function(t){return e[t]}.bind(null,n));return r},a.n=function(e){var t=e&&e.__esModule?function(){return e["default"]}:function(){return e};return a.d(t,"a",t),t},a.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},a.p="/";var p=window["webpackJsonp"]=window["webpackJsonp"]||[],l=p.push.bind(p);p.push=t,p=p.slice();for(var s=0;s<p.length;s++)t(p[s]);var d=l;o.push([0,"chunk-vendors"]),r()})({0:function(e,t,r){e.exports=r("56d7")},"56d7":function(e,t,r){"use strict";r.r(t);var n=r("2b0e"),i=function(){var e=this,t=e.$createElement,r=e._self._c||t;return r("div",{attrs:{id:"pixi-canvas"}})},o=[],a=r("912c"),p=r("b2c3"),l={name:"layout",data(){return{app:null,viewport:null,container:null,Application:a["Application"],loader:a["loader"],Sprite:a["Sprite"],tiles:[]}},mounted(){this.app=new this.Application({width:953,height:409,backgroundColor:16777215}),this.viewport=new p["a"]({screenWidth:953,screenHeight:409,worldWidth:25e3,worldHeight:1e4,interaction:this.app.renderer.plugins.interaction}),this.container=new a["ParticleContainer"];const e=document.querySelector("#pixi-canvas");e.appendChild(this.app.view),this.app.stage.addChild(this.viewport),this.viewport.addChild(this.container),this.viewport.drag().pinch().wheel().decelerate(),this.viewport.on("clicked",e=>{if(e.world.x>0&&e.world.y>0){const t=32*Math.floor(e.world.x/32),r=32*Math.floor(e.world.y/32);this.drawNewTile(t,r)}}),this.app.loader.add("maptiles","api/map/random",{xhrType:"json"}).load((e,t)=>{let r=t.maptiles.data.tiles;const n=new a["Container"];this.viewport.addChild(n);const i=a["Texture"].from("assets/terrains/ground.bmp"),o=a["Texture"].from("assets/terrains/sand.bmp");r.forEach(e=>{let t=null;t="GROUND"==e.terrain?new a["Sprite"](i):new a["Sprite"](o),t.anchor.set(.5),t.x=40*e.x+20,t.y=40*e.y+20,n.addChild(t)}),this.app.start()}),this.app.stop()},methods:{drawNewTile(e,t){const r=new a["Sprite"](a["Texture"].WHITE);r.x=e,r.y=t,r.width=r.height=25,r.tint=12704739,r.interactive=!0,r.buttonMode=!0,this.viewport.addChild(r)}}},s=l,d=r("2877"),c=Object(d["a"])(s,i,o,!1,null,"6d437f39",null),u=c.exports;n["a"].config.productionTip=!1,new n["a"]({render:e=>e(u)}).$mount("#app")}});
//# sourceMappingURL=app.0af839eb.js.map