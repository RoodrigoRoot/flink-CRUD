
ui = new UICompanies()

document.addEventListener('load', ui.UICreatecompany() )

form_company = document.getElementById("form_company")
name_company = document.getElementById("name")
description = document.getElementById("description")
symbol = document.getElementById("symbol")
market_values = document.getElementById("market_values")
form_company.addEventListener('submit', (e)=> ui.UIValidateCompany(e))

company_list = document.querySelector('.company_list')
company_list.addEventListener('click', (e)=> ui.actionsCompany(e))