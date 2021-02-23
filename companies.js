class Companies{

    url = "http://localhost:8000/api/v1/companies/"

    async getCompanies(){
        let response = await fetch(this.url)
        const companies = await response.json();
        return companies
    }

    async SendDataForm(e){
        e.preventDefault()
        
        let request = await fetch(this.url,
        {
            method:'POST',
            headers:{
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                name:name_company.value,
                description:description.value,
                symbol:symbol.value,
                market_values:[market_values.value]
            })
        })
        return request
    
    }

    /*async actionsCompany(e){
        e.preventDefault()
        company_list.addEventListener('click', function(e){
            let btn_delete_pressed = e.target.id == 'delete-company'
            let btn_update_pressed = e.target.id == 'update-company'
            let id = e.target.parentElement.dataset.id
        
            if(btn_delete_pressed){
                let response = await fetch(`${url}/${id}`,
                {
                    method:'DELETE',
                }
                )
                console.log(await response.json())
                return "ok"
                
            }
            else if(btn_update_pressed){
                console.log(e.target.parentElement.dataset.id)
            }
        })

    }*/
}