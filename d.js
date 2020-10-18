function updatedata(){
    var data =JSON.parse(localStorage.getItem('data'));
        
             if(data.success==1){
         
                document.getElementById("username1").innerHTML=`
                    <p class="mb-1 text-black">${data.user_info.username}</p>`
                 document.getElementById("username2").innerHTML=`
                 <span class="font-weight-bold mb-2">${data.user_info.username}</span>
                    <span>${data.user_info.email}</span>`
                
                
                 document.getElementById("dashboard-product-div").innerHTML =`
                        ${data.products_info.map(populateProduct).join(" ")}`
                 
                 
                 document.getElementById("price-notifs").innerHTML=`
                        ${data.notifs.map(populateNotifs).join(" ")}`
                 if(data.notifs.length!=0){
                     document.getElementById("bell-high").innerHTML=`<span class="count-symbol bg-danger"></span>`
    }
    }
     else{
         window.location.replace("http://127.0.0.1:5000");
     }
     $.post("http://127.0.0.1:5000/dashboard",data.user_info,function(str){
                        localStorage.clear()
         
                       localStorage.setItem('data', JSON.stringify(str)); 
         
                        var jsondata = JSON.parse(localStorage.getItem('data'));
         if(jsondata.success==1){
             
                 document.getElementById("dashboard-product-div").innerHTML =`
                        ${jsondata.products_info.map(populateProduct).join(" ")}`
                 
                 
                 document.getElementById("price-notifs").innerHTML=`
                        ${jsondata.notifs.map(populateNotifs).join(" ")}`
                 if(jsondata.notifs.length!=0){
                     document.getElementById("bell-high").innerHTML=`<span class="count-symbol bg-danger"></span>`
    }
    }
     else{
         window.location.replace("http://127.0.0.1:5000");
     }});
    
}
    function colorCard(product){
                    if(product.price_init > product.price_update)
                        {
                            return `success`
                        }
                    else if(product.price_init == product.price_update)
                        {
                            return `info`
                        }
                    else
                        {
                            return `danger`
                        }
                }
    function populateProduct(product){
                     return `
                            <div class="col-md-4 stretch-card grid-margin">
                                <div class="card bg-gradient-${colorCard(product)} card-img-holder text-white">
                                    <div class="card-body">
                                        
                                            <h4 class="font-weight-normal mb-3">${product.product_name}...
                                         </h4>
                                        <h4 class="mb-5">₹ ${product.price_update}</h4>
                                        <a href="${product.aff_url}"><button class="add btn btn-info btn-icon-text float-right"> Buy Now<i class="mdi mdi-cart-outline btn-icon-append"></i> </button> </a>
                                      </div>
                                    </div>
                                  </div>`
                }
    
    function populateNotifs(notif){
                    return `
                        <a class="dropdown-item preview-item" href="${notif.aff_url}">
                      <div class="preview-thumbnail">
                        <div class="preview-icon bg-success">
                          <i class="mdi mdi-check-all"></i>
                        </div>
                      </div>
                      <div class="preview-item-content d-flex align-items-start flex-column justify-content-center">
                        <h6 class="preview-subject font-weight-normal mb-1">Price of ${notif.product_name}... has just dropped to ₹${notif.price_update}</h6>
                        </div>
                    </a>
                    <div class="dropdown-divider"></div>
    `
    }
    
                 
    function signout(){
              localStorage.clear();
                localStorage.setItem("success",0);
               window.location.replace("../index.html");   
          }