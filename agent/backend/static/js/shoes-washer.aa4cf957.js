(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["shoes-washer"],{"5fbe":function(t,s,e){t.exports=e.p+"img/logo2.88467ec1.png"},"679c":function(t,s,e){t.exports=e.p+"img/card.e18f66c7.png"},"835c":function(t,s,e){},"87e1":function(t,s,e){},dfc3:function(t,s,e){"use strict";var a=e("835c"),n=e.n(a);n.a},e6da:function(t,s,e){t.exports=e.p+"img/cash.b45b4be8.png"},ecb6:function(t,s,e){"use strict";e.r(s);var a=function(){var t=this,s=t.$createElement,a=t._self._c||s;return a("v-layout",{attrs:{wrap:""}},[a("v-flex",{attrs:{xs12:""}},[a("v-stepper",{staticClass:"wt-stepper elevation-0",attrs:{"alt-labels":""},model:{value:t.steps,callback:function(s){t.steps=s},expression:"steps"}},[a("v-stepper-header",[a("v-stepper-step",{staticClass:"single-stepper",class:"ko"!=t.$i18n.locale?"body-2":t.$store.getters.isV2?"headline":"display-1",attrs:{complete:!0,step:"1"}},[t._v(t._s(t.$t("shoes-washer.step2.title")))])],1),a("v-stepper-items",[a("v-stepper-content",{attrs:{step:"1"}},[a("step2",{attrs:{selected:t.selected,steps:t.steps,dialog:t.dialog,price:t.price},on:{"update:selected":function(s){t.selected=s},"update:steps":function(s){t.steps=s},"update:dialog":function(s){t.dialog=s},"update:price":function(s){t.price=s}}}),a("v-layout",{attrs:{"justify-space-between":""}},[a("v-flex",{staticClass:"text-xs-center",attrs:{xs3:""}}),a("v-flex",{staticClass:"text-xs-center",attrs:{xs3:""}},[a("img",{staticClass:"wt-bottom-logo",attrs:{src:e("5fbe")}})]),a("v-flex",{attrs:{xs3:""}})],1)],1)],1)],1)],1),a("v-dialog",{attrs:{lazy:"",persistent:t.paymentSteps>=5},model:{value:t.dialog,callback:function(s){t.dialog=s},expression:"dialog"}},[a("v-card",{attrs:{height:"800px"}},[a("v-card-title",[a("v-spacer"),t.paymentSteps<5?a("v-btn",{attrs:{flat:"",icon:""},on:{click:function(s){return t.clearDialog()}}},[a("v-icon",{staticClass:"fa fa-times fa-4x"})],1):t._e()],1),a("v-card-text",[1===t.paymentSteps?a("v-layout",{attrs:{wrap:"","justify-center":"","align-center":"","mt-5":""}},[a("v-flex",{staticClass:"text-xs-center",attrs:{xs12:"","mt-5":""}},[a("p",[a("span",{staticClass:"display-2"},[t._v(t._s(t.$t("payment.shoes-washer")))]),a("br"),a("span",{staticClass:"display-2"},[t._v(t._s(t.$t("payment.desc2-3")))]),a("br"),a("br"),a("span",{directives:[{name:"show",rawName:"v-show",value:!t.canPayment(),expression:"!canPayment()"}],staticClass:"display-2 mt-5",attrs:{"mt-3":""}},[t._v('\n                "'+t._s(t.$t("payment.cant-payment"))+'"\n              ')])])]),a("v-flex",{staticClass:"text-xs-center mt-5",attrs:{xs6:""}},[a("v-btn",{staticClass:"display-2 wt-wave-bg wt-btn white--text py-5",attrs:{round:"",disabled:!t.canPayment()},on:{click:function(s){t.$store.state.user.hasOwnProperty("phone")?t.trigger():t.paymentSteps=2}}},[t.canPayment()?a("span",[t._v(t._s(t.$t("app.buy")))]):a("span",[t._v(t._s(t.$t("payment.no-payment")))])])],1)],1):2===t.paymentSteps?a("v-layout",{attrs:{wrap:"","justify-center":"","align-center":"","mt-5":""}},[a("v-flex",{staticClass:"text-xs-center",attrs:{xs12:""}},[a("p",[a("span",{staticClass:"display-2"},[t._v(t._s(t.$t("payment.way")))])])]),a("v-flex",{staticClass:"text-xs-center mt-5",attrs:{xs6:""}},[a("v-btn",{staticClass:"display-3 huge-btn white--text",attrs:{color:"#ea68a2",round:""},on:{click:function(s){t.paymentSteps=4,t.payment="cash"}}},[a("p",[a("img",{attrs:{src:e("e6da")}}),a("br"),a("span",[t._v(t._s(t.$t("payment.cash")))])])])],1),a("v-flex",{staticClass:"text-xs-center mt-5",attrs:{xs6:""}},[a("v-btn",{directives:[{name:"show",rawName:"v-show",value:!0===t.$store.state.agency.menu_card,expression:"$store.state.agency.menu_card === true"}],staticClass:"display-3 huge-btn white--text",attrs:{color:"#ea68a2",round:""},on:{click:function(s){t.paymentSteps=3,t.payment="card"}}},[a("p",[a("img",{attrs:{src:e("679c")}}),a("br"),a("span",[t._v(t._s(t.$t("payment.card")))])])])],1)],1):3===t.paymentSteps?a("v-layout",{attrs:{wrap:"","justify-center":"","align-center":"","mt-5":""}},[a("v-flex",{staticClass:"text-xs-center",attrs:{xs12:"","mb-5":""}},[a("p",[a("span",{staticClass:"display-2"},[t._v(t._s(t.$t("payment.desc5")))])])]),t._l(t.prices,function(s){return a("v-flex",{key:s,staticClass:"text-xs-center mt-1",attrs:{xs5:""}},[a("v-btn",{staticClass:"display-1 wt-payment-btn",attrs:{round:""},on:{click:function(e){t.paymentSteps=4,t.paymentPrice=s}}},[a("span",[t._v(t._s(s)+" "+t._s(t.$t("app.money-unit")))])])],1)})],2):4===t.paymentSteps&&"ko"===t.$i18n.locale?a("v-layout",{attrs:{wrap:"","justify-center":"","align-center":"","mt-5":""}},[a("v-flex",{staticClass:"text-xs-left",attrs:{xs8:""}},[a("span",{staticClass:"display-2"},[t._v(t._s(t.$t("payment.product-price"))+": ")]),a("span",{staticClass:"display-2 wt-primary-font"},[t._v(t._s(t.price))]),a("span",{staticClass:"display-2"},[t._v(t._s(t.$t("app.money-unit")))])]),"card"===t.payment?a("v-flex",{staticClass:"text-xs-left",attrs:{xs8:"","mt-3":""}},[a("span",{staticClass:"display-2"},[t._v(t._s(t.$t("payment.payment-price"))+": ")]),a("span",{staticClass:"display-2 wt-primary-font"},[t._v(t._s(t.paymentPrice))]),a("span",{staticClass:"display-2"},[t._v(t._s(t.$t("app.point-unit")))])]):t._e(),a("v-flex",{staticClass:"text-xs-left",attrs:{xs9:"","my-2":""}},[a("v-divider")],1),a("v-flex",{staticClass:"text-xs-left",attrs:{xs8:"","mt-3":""}},[a("span",{staticClass:"display-2"},[t._v(t._s(t.$t("payment.total-saved-money"))+": ")]),a("span",{staticClass:"display-2 wt-primary-font"},[t._v("0")]),a("span",{staticClass:"display-2"},[t._v("\n              "+t._s(t.$t("app.money-unit"))+"\n              "),a("br"),t._v("\n              "+t._s(t.$t("payment.cant-save"))+"\n            ")])]),a("v-flex",{staticClass:"text-xs-center",attrs:{xs6:"","mt-4":""}},[a("v-btn",{staticClass:"display-2 wt-wave-bg wt-btn white--text py-5",attrs:{round:"",disabled:"card"===t.payment&&t.paymentPrice<t.course.amount},on:{click:function(s){t.requestPayment(),t.paymentSteps=5}}},["card"===t.payment?a("span",[t._v(t._s(t.$t("payment.card")))]):a("span",[t._v(t._s(t.$t("payment.cash")))])])],1)],1):4===t.paymentSteps&&"ko"!==t.$i18n.locale?a("v-layout",{attrs:{wrap:"","justify-center":"","align-center":"","mt-5":""}},[a("v-flex",{staticClass:"text-xs-left",attrs:{xs8:""}},[a("span",{staticClass:"display-1"},[t._v(t._s(t.$t("payment.product-price"))+": ")]),a("span",{staticClass:"display-1 wt-primary-font"},[t._v(t._s(t.price))]),a("span",{staticClass:"display-1"},[t._v(t._s(t.$t("app.money-unit")))])]),"card"===t.payment?a("v-flex",{staticClass:"text-xs-left",attrs:{xs8:"","mt-3":""}},[a("span",{staticClass:"display-1"},[t._v(t._s(t.$t("payment.payment-price"))+": ")]),a("span",{staticClass:"display-1 wt-primary-font"},[t._v(t._s(t.paymentPrice))]),a("span",{staticClass:"display-1"},[t._v(t._s(t.$t("app.point-unit")))])]):t._e(),a("v-flex",{staticClass:"text-xs-left",attrs:{xs9:"","my-2":""}},[a("v-divider")],1),a("v-flex",{staticClass:"text-xs-left",attrs:{xs8:"","mt-3":""}},[a("span",{staticClass:"display-1"},[t._v(t._s(t.$t("payment.total-saved-money"))+": ")]),a("span",{staticClass:"display-1 wt-primary-font"},[t._v("0")]),a("span",{staticClass:"display-1"},[t._v("\n              "+t._s(t.$t("app.money-unit"))+"\n              "),a("br"),t._v("\n              "+t._s(t.$t("payment.cant-save"))+"\n            ")])]),a("v-flex",{staticClass:"text-xs-center",attrs:{xs6:"","mt-4":""}},[a("v-btn",{staticClass:"display-1 wt-wave-bg wt-btn white--text py-5",attrs:{round:"",disabled:"card"===t.payment&&t.paymentPrice<t.price},on:{click:function(s){t.requestPayment(),t.paymentSteps=5}}},["card"===t.payment?a("span",[t._v(t._s(t.$t("payment.card")))]):a("span",[t._v(t._s(t.$t("payment.cash")))])])],1)],1):5===t.paymentSteps?a("v-layout",{attrs:{wrap:"","justify-center":"","align-center":"","mt-5":""}},["cash"===t.payment?a("v-flex",{staticClass:"text-xs-left",attrs:{xs8:"","mt-3":""}},[a("span",{staticClass:"display-2"},[t._v(t._s(t.$t("payment.cash-warning")))])]):t._e(),a("v-flex",{staticClass:"text-xs-left",attrs:{xs8:"","mt-3":""}},[a("span",{staticClass:"display-2"},[t._v(t._s(t.$t("payment.payment-price"))+": ")]),a("span",{staticClass:"display-2 wt-primary-font"},[t._v(t._s(t.price))]),a("span",{staticClass:"display-2"},[t._v(t._s(t.$t("app.money-unit")))])]),a("v-flex",{staticClass:"text-xs-left",attrs:{xs8:"","mt-3":""}},[a("span",{staticClass:"display-2"},[t._v(t._s(t.$t("payment.insert-money"))+": ")]),a("span",{staticClass:"display-2 wt-primary-font"},[t._v(t._s(t.insertMoney))]),a("span",{staticClass:"display-2"},[t._v(t._s(t.$t("app.money-unit")))])]),a("v-flex",{staticClass:"text-xs-left",attrs:{xs8:"","mt-3":""}},[a("span",{staticClass:"display-2"},[t._v(t._s(t.$t("payment.limit-time"))+": ")]),a("span",{staticClass:"display-2 wt-primary-font"},[t._v(t._s(120-t.insertCount))]),a("span",{staticClass:"display-2"},[t._v(t._s(t.$t("app.second")))])])],1):6===t.paymentSteps?a("v-layout",{attrs:{wrap:"","justify-center":"","align-center":"","mt-5":""}},[a("v-flex",{staticClass:"text-xs-center",attrs:{xs8:"","mt-3":""}},[a("span",{staticClass:"display-2"},[t._v(t._s(t.$t("payment.failure")))])]),a("v-flex",{staticClass:"text-xs-center",attrs:{xs8:"","mt-3":""}},[a("span",{staticClass:"display-1"},[t._v(t._s(t.$t("payment.close")))])])],1):7===t.paymentSteps?a("v-layout",{attrs:{wrap:"","justify-center":"","align-center":"","mt-5":""}},[a("v-flex",{staticClass:"text-xs-center",attrs:{xs8:"","mt-3":""}},[a("span",{staticClass:"display-1"},[t._v(t._s(t.$t("payment.shoes-washer-success")))])]),a("v-flex",{staticClass:"text-xs-center",attrs:{xs8:"","mt-3":""}},[a("span",{staticClass:"display-1"},[t._v(t._s(t.$t("payment.close")))])])],1):t._e()],1)],1)],1)],1)},n=[],i=function(){var t=this,s=t.$createElement,e=t._self._c||s;return e("v-card",{staticClass:"mb-5 elevation-0",attrs:{height:"640px"}},[e("v-layout",{attrs:{wrap:"","justify-center":"","align-center":"","fill-height":""}},["ko"===t.$i18n.locale?e("v-flex",{staticClass:"text-xs-center",attrs:{xs12:"","pa-1":""}},[e("span",{staticClass:"display-2"},[t._v(t._s(t.$t("shoes-washer.step2.desc1"))+" ")]),e("span",{staticClass:"display-2 font-weight-bold wt-primary-font"},[t._v(t._s(t.$t("shoes-washer.step2.desc2")))]),e("span",{staticClass:"display-2"},[t._v(t._s(t.$t("shoes-washer.step2.desc3")))])]):e("v-flex",{staticClass:"text-xs-center",attrs:{xs12:"","pa-1":""}},[e("span",{staticClass:"display-1"},[t._v(t._s(t.$t("shoes-washer.step2.desc1"))+" ")]),e("span",{staticClass:"display-1"},[t._v(t._s(t.$t("shoes-washer.step2.desc2"))+" ")]),e("span",{staticClass:"display-1"},[t._v(t._s(t.$t("shoes-washer.step2.desc3")))])]),t._l(t.items,function(s,a){return e("v-flex",{key:s.id,staticClass:"text-xs-center",attrs:{xs4:"","pa-1":""}},[e("v-btn",{staticClass:"washer",class:a==t.selected?"selected-washer":"not-selected-washer",attrs:{flat:"",top:""},on:{click:function(s){return t.selectWasher(a)}}},[e("v-layout",{attrs:{wrap:"","mb-5":""}},[e("v-flex",{attrs:{xs12:""}},[e("span",{staticClass:"display-1"},[t._v(t._s(t.$t("shoes-washer.step2.select",{number:s.controller_id})))])])],1)],1)],1)})],2)],1)},r=[],c={name:"ShoesWasherStep2",props:{selected:Number,steps:Number,dialog:Boolean},data:function(){return{unitPrice:0,maxPrice:0,minPrice:0,unit:0}},computed:{items:function(){return this.$store.state.devices["shoes-washer"]}},methods:{selectWasher:function(t){this.$emit("update:selected",t),this.$emit("update:dialog",!0)}},watch:{selected:function(t){if(null!==t){var s=this.$store.state.devices["shoes-washer"][t];this.unit=s.min_etc_coin,this.unitPrice=s.min_coin,this.maxPrice=s.max_coin,this.minPrice=s.current_coin,this.$emit("update:minutes",this.unit*(this.minPrice/this.unitPrice)),this.$emit("update:price",this.minPrice)}}},mounted:function(){if(null!==this.selected){var t=this.$store.state.devices["shoes-washer"][this.selected];this.unit=t.min_etc_coin,this.unitPrice=t.min_coin,this.maxPrice=t.max_coin,this.minPrice=t.current_coin,this.$emit("update:minutes",this.unit*(this.minPrice/this.unitPrice)),this.$emit("update:price",this.minPrice)}}},p=c,l=(e("dfc3"),e("2877")),o=Object(l["a"])(p,i,r,!1,null,"df6a2e9c",null),m=o.exports,y={name:"ShoesWasher",components:{Step2:m},data:function(){return{minutes:0,price:0,steps:1,selected:null,dialog:!1,payment:null,paymentSteps:1,paymentPrice:0,prices:[1e3,5e3,1e4,2e4,3e4,4e4,5e4],interval:null,insertMoney:0,insertCount:0}},destroyed:function(){this.clearDialog(),this.interval&&clearInterval(this.interval)},methods:{canPayment:function(){if(!this.$store.state.user.hasOwnProperty("phone"))return!0;if(0!==this.$store.state.agency.use_point&&this.$store.state.user.point>=this.$store.state.agency.use_point){if(this.$store.state.user.point+this.$store.state.user.money>=this.price)return!0}else if(this.$store.state.user.money>=this.price)return!0;return!1},trigger:function(){var t=this;if(this.$store.commit("statePause",!0),this.interval&&clearInterval(this.interval),this.insertMoney<this.paymentPrice)return this.paymentSteps=6,void setTimeout(function(){this.clearDialog()},2e3);var s=this.$store.state.devices["shoes-washer"][this.selected].controller_id;this.$axios.post("/trigger",{price:this.price,target:s}).then(function(s){if(t.$store.state.user.hasOwnProperty("phone")){var e=0,a=0;if(e=t.$store.state.user.point<t.$store.state.agency.use_point?0:t.$store.state.user.point>=t.price?t.price:t.$store.state.user.point,!(t.$store.state.user.money>=t.price-e))return t.paymentSteps=6,void setTimeout(t.clearDialog,2e3);a=t.price-e,console.log(e,a),t.$store.state.user.point-=e,t.$store.state.user.money-=a,t.$axios.post("/server",{method:"POST",path:"/payment",args:{agency_id:t.$store.state.agency.id,member_id:t.$store.state.user.id,amount:a,use_point:e,pay_type:3,device_type:3}})}else t.$axios.post("/server",{method:"POST",path:"/payment",args:{agency_id:t.$store.state.agency.id,member_id:0,amount:t.insertMoney,pay_type:"cash"===t.payment?0:2,device_type:3}});t.paymentSteps=7,setTimeout(function(){this.$router.push("/first"),this.clearDialog()}.bind(t),5e3)}).catch(function(s){t.paymentSteps=6,setTimeout(t.clearDialog,2e3)})},clearDialog:function(){this.$store.commit("stateNoAction",60),this.$store.commit("statePause",!1),this.dialog=!1,this.paymentSteps=1,this.paymentPrice=0,this.insertMoney=0,this.insertCount=0},requestPayment:function(){var t=this;this.$store.commit("statePause",!0),"cash"===this.payment?(this.$axios.post("/cash/call").then(function(s){t.insertMoney=s.data.money}).catch(function(s){t.interval&&clearInterval(t.interval),t.$socket.emit("cancel-payment")}),this.interval=setInterval(function(){var t=this;this.$axios.get("/cash/status").then(function(s){s.data.money>=t.price?(t.trigger(),t.$socket.emit("cancel-payment")):(s.data.money&&(t.insertMoney=s.data.money),s.data.t&&(t.insertCount=s.data.t))}).catch(function(t){})}.bind(this),500)):"card"===this.payment&&(this.$axios.post("/card/call",{money:this.paymentPrice}).then(function(s){t.insertMoney=s.data.money,t.trigger()}).catch(function(t){}).finally(function(){t.interval&&clearInterval(t.interval)}),this.interval=setInterval(function(){var t=this;this.$axios.get("/card/status").then(function(s){s.data.money<t.paymentPrice&&(s.data.money&&(t.insertMoney=s.data.money),s.data.t&&(t.insertCount=s.data.t))}).catch(function(t){})}.bind(this),500))}}},u=y,d=(e("fcec"),Object(l["a"])(u,a,n,!1,null,"e2ad02b4",null));s["default"]=d.exports},fcec:function(t,s,e){"use strict";var a=e("87e1"),n=e.n(a);n.a}}]);
//# sourceMappingURL=shoes-washer.aa4cf957.js.map