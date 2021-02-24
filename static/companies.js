class Companies{

    url = "http://localhost:8000/api/v1/companies/"

    async getCompanies(){
        
        let response = await fetch(this.url)
        const companies = await response.json();
        return companies
    }

    async SendDataForm(e){
        e.preventDefault()
        let csrftoken = this.getCookie('csrftoken');
        let request = await fetch(this.url,
        {
            method:'POST',
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
        return request
    
    }



    
    getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    

}