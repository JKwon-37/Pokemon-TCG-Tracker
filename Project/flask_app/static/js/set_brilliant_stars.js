let pokeForm = document.querySelector('#singles')

pokeForm.addEventListener('submit', function(event){
    event.preventDefault()
    let cardNumber = event.target.children[0].value;

    fetch(`https://api.pokemontcg.io/v2/cards?q=set.id:swsh9&APPID=5f4b4281-1095-4b93-a346-c24372a904b5`)
    
      .then((response) => response.json())
      .then(data => {
        
        console.log(data.data[`${cardNumber}`]);

        // Data pulled from Pokemon TCG API
        let imgURL = data.data[`${cardNumber-1}`].images.small
        let cardName = data.data[`${cardNumber-1}`].name
        let marketPrice = data.data[`${cardNumber-1}`].cardmarket.prices.averageSellPrice
        let rarity = data.data[`${cardNumber-1}`].rarity
        let set = data.data[`${cardNumber-1}`].set.name
        

        // Query selectors
        let pokeImgDiv = document.querySelector('#pokeimg')
        let cardNameDiv = document.querySelector('#cardName')
        let marketPriceDiv = document.querySelector('#marketPrice')
        let rarityDiv = document.querySelector('#rarity')
        let setDiv = document.querySelector('#set')

        // Load attributes from Pokemon TCG API
        pokeImgDiv.innerHTML = `
        <img src="${imgURL}" alt="card-img">`
        cardNameDiv.innerHTML = `
        <h1>${cardName}</h1>`
        marketPriceDiv.innerHTML = `
        <h1>TCG Player Average Sell Price: $    ${marketPrice}</h1>`
        rarityDiv.innerHTML = `
        <h1>Rarity: ${rarity}</h1>`
        setDiv.innerHTML = `
        <h1>Set: ${set}</h1>`
      })
})




