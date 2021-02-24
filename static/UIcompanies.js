class UICompanies{

    company = new Companies()

    url = "http://localhost:8000/api/v1/companies"
    async UICreatecompany(){
        let company_response = await this.company.getCompanies()
        let company_article = document.getElementById("companies_data");
        company_response.map( (item, index)=>{
        let div = document.createElement('div') 
        div.className="card mb-3"
        div.innerHTML=`
        <div  class="card-body" data-id=${item.auto_id}>
        <h4 class="card-title">${String(item.name).toLocaleUpperCase()} </h4>
        <p class="symbol">${item.symbol}</p>
        <p class="description">${item.description}</p>
        <p class="market_values">${item.market_values}</p>
        
        <a class="card-link" href="#" id="delete-company">Eliminar</a>
        <a class="card-link" href="#" id="update-company">Modificar</a>
        </div>
        </div>
        `
        company_article.appendChild(div);          
      
        } )
        

    }

    async UIValidateCompany(e){
        let request = await this.company.SendDataForm(e)
        if(request.ok){
            alert("Company Created");
            location.reload();
        }else{
            let validations = await request.json();            
            if(validations.name){
                let name_errors = document.getElementById("name_errors")
                let div = document.createElement('div') 
                div.className='alert alert-danger'
                div.innerHTML=`<p> ${validations.name}</p>`
                name_errors.appendChild(div);
            }


            if(validations.description){
                let description_errors = document.getElementById("description_errors")
                let div_description = document.createElement('div') 
                div_description.className='alert alert-danger'
                div_description.innerHTML=`<p> ${validations.description}</p>`
                description_errors.appendChild(div);
            }

            if(validations.symbol){
                let symbol_errors = document.getElementById("symbol_errors")
                let div_symbol = document.createElement('div') 
                div_symbol.className='alert alert-danger'
                div_symbol.innerHTML=`<p> ${validations.symbol}</p>`
                symbol_errors.appendChild(div_symbol);
            }

            if(validations.div_market_values){
                let market_values_errors = document.getElementById("market_values_errors")
                let div_market_values_errors = document.createElement('div') 
                div_market_values_errors.className='alert alert-danger'
                div_market_values_errors.innerHTML=`<p> ${validations.symbol}</p>`
                market_values_errors.appendChild(div_symbol);
            }

        }
    
    }

       actionsCompany(e){
        company_list.addEventListener('click', this.deleteAndUpdateCompany(e));
    }

    async deleteAndUpdateCompany(e){
        
            let btn_delete_pressed = e.target.id == 'delete-company';
            let btn_update_pressed = e.target.id == 'update-company';
            let id = e.target.parentElement.dataset.id;
            var csrftoken = this.company.getCookie('csrftoken');
            console.log(btn_delete_pressed)
            if(btn_delete_pressed){
                let response = await fetch(`${this.url}/${id}`,
                {
                    headers: {
                        'Accept': 'application/json',
                        'Content-Type': 'application/json',
                        'X-CSRFToken': csrftoken
                      },
                    method:'DELETE',
                });
                location.reload()

                
            }
            else if(btn_update_pressed){
                const parent = e.target.parentElement
                let name_company_update = parent.querySelector('.card-title').textContent;
                let description_company_update = parent.querySelector('.description').textContent;
                let symbol_company_update = parent.querySelector('.symbol').textContent;
                let market_values_company_update = parent.querySelector('.market_values').textContent;

                name_company.value = name_company_update
                description.value = description_company_update
                symbol.value = symbol_company_update
                market_values.value = market_values_company_update
                btn_form.value="Update"

                btn_form.addEventListener('click', async (e)=>{
                    e.preventDefault()
                    let response = await fetch(`${this.url}/${id}`,{
                        method:'PATCH',
                        headers: {
                            'Accept': 'application/json',
                            'Content-Type': 'application/json',
                            'X-CSRFToken': csrftoken
                          },
                        body: JSON.stringify({
                            name:name_company.value,
                            description:description.value,
                            symbol:symbol.value,
                            market_values:[market_values.value]
                        })
                    })
                })
            }
        
    }


}