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

}