let botao = window.document.getElementById('btn');
let quebrou = false;
let cc = 0;
botao.style.background = 'blue';

botao.addEventListener('mouseover', e => {
    if (!quebrou) {
        botao.style.background = 'green';
        botao.innerHTML = `Clicou ${cc} vezes!`;
    }
})

botao.addEventListener('click', e => {
    cc++;
    botao.innerHTML = `Clicou ${cc} vezes!`;
    if (cc >= 10) {
        quebrou = true;
        botao.innerText = 'Quebrei!';
        botao.style.background = 'red';
    }   
});

botao.addEventListener('mouseout', e => {
    // caso não precise chamar essa função em outros momentos, pode-se usar esse comando acima
    if (!quebrou) {
        botao.style.background = 'blue';
        botao.innerText = 'Clique em Mim';
    }
})