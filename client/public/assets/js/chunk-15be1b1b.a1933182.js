(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-15be1b1b"],{"60b9":function(t,a,n){"use strict";var s=n("76b4"),o=n.n(s);o.a},"76b4":function(t,a,n){},d310:function(t,a,n){"use strict";n.r(a);var s=function(){var t=this,a=t.$createElement,n=t._self._c||a;return n("div",{staticClass:"informes-lista"},[n("b-container",[n("div",{staticClass:"row justify-content-center"},[n("div",{staticClass:"col-9 p-4"},[n("h1",{staticClass:"titulo"},[t._v(" Informes ")]),this.$root.logado&&this.$root.admin?n("b-button",{attrs:{to:"informes/novo",size:"sm",variant:"dark"}},[n("b-icon",{attrs:{icon:"plus"}}),t._v(" Novo informe ")],1):t._e(),t._l(t.posts_atuais,(function(a){return n("div",{key:a.id,staticClass:"row-2 my-3"},[n("Informe",{attrs:{post_info:a,esconder_texto:t.esconder_texto}})],1)})),n("b-pagination",{staticClass:"justify-content-center",attrs:{"total-rows":t.total_posts,"per-page":t.por_pagina},model:{value:t.pagina_atual,callback:function(a){t.pagina_atual=a},expression:"pagina_atual"}})],2)])])],1)},o=[],i=(n("fb6a"),n("8403")),e=n("bc3a"),r={components:{Informe:i["a"]},data:function(){return{posts:[],pagina_atual:1,por_pagina:5,esconder_texto:!0}},computed:{total_posts:function(){return this.posts.length},posts_atuais:function(){return this.posts.slice((this.pagina_atual-1)*this.por_pagina,this.pagina_atual*this.por_pagina)}},created:function(){this.getPosts()},methods:{getPosts:function(){var t=this;e.get("/api/informes").then((function(a){t.posts=a.data.conteudo})).catch((function(t){alert(t)}))}}},c=r,u=(n("60b9"),n("2877")),p=Object(u["a"])(c,s,o,!1,null,null,null);a["default"]=p.exports}}]);
//# sourceMappingURL=chunk-15be1b1b.a1933182.js.map