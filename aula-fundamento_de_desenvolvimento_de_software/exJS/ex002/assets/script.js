// captar os dois inputs
// captar o operador
// fazer a operação especficada com os dois inputs
// mostrar o resultado na tela
function calc() {
    let str1 = window.document.querySelector('#n1');
    let num1 = Number(str1.value);
    let str2 = window.document.querySelector('#n2');
    let num2 = Number(str2.value);
    let opt = window.document.querySelector('#op').value;
    let rtd = window.document.querySelector('#res');
    let op;

    if (str1.value === '' || str2.value == '') {
        rtd.classList.add('problema');
        rtd.innerHTML = 'Um ou mais campos estão vazios';
        setTimeout(() => {
            rtd.classList.remove('problema');
            rtd.innerHTML = '';
        }, 3000)
        return;
    } else {
        if (opt === '+') {
            op = num1 + num2;
        } else if (opt === '-') {
            op = num1 - num2;
        } else if (opt === '/') {
            op = num1 * num2;
        } else {
            op = num1 / num2;
        }
    }

    rtd.innerHTML = op;
}