function changeCouleur()
{
    const coul = document.body.style.backgroundColor;
    /* Au chargement de la page, le navigateur crée un document
     * on parle de DOM (Document Objet Model)
     * Le modèle DOM HTML est construit comme une arborescence d'objets*/
    if (coul === 'orange')
    {
        document.body.style.backgroundColor = 'blue';
    }
    else
    {
        document.body.style.backgroundColor = 'orange';
    }
}

function choixLangue()
{
    const choix = document.getElementById("choix");
    const monChoix = choix[choix.selectedIndex];
    alert(’Vous allez choisir ’ + monChoix.text + ’ soit ’ + monChoix.value);
}
