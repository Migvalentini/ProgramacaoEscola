const submitInput = document.querySelector('#submit-input')

submitInput.addEventListener('click', (ev) => {
   ev.preventDefault()
   const ul = document.querySelector('#list')
   const number = document.querySelector('#number-input').value
   const mainLi = document.createElement('li')
   const br = document.createElement('br')
   ul.textContent= ''
   mainLi.textContent = `Número: ${number}`
   if (number) {
      ul.append(mainLi, br)
      for (let index = 1; index <= 10; index++) {
         const newLi = document.createElement('li')
         newLi.textContent = `${number} x ${index} = ${Math.round(number * index)}`
         ul.appendChild(newLi)
      }
   } else {
      const errorAlert = document.createElement('li')
      errorAlert.textContent = `Por favor, digite um número...`
      ul.appendChild(errorAlert)
   }
})