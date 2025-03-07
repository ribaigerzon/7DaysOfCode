# -*- coding: utf-8 -*-
"""ONE-JS-dias-1y2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1OXz4EbZENnJwkQh5zXXe_U4RwNU_yGCe

La parte más confusa para quienes están comenzando a aprender lógica con JavaScript es la operación de igualdad entre valores. Dependiendo de cómo escribas tu código, JavaScript hará una conversión de tipo a un tipo booleano de manera implícita (automática), y esto afectará a variables que eran Strings, Numbers, Object, etc.

Esto causa algunos comportamientos extraños, como todos estos ejemplos a continuación que retornan true:

console.log( false == '0' );
console.log( null == undefined );
console.log( " \t\r\n" == 0 );
console.log( ' ' == 0 );

Lo cual no tiene necesariamente mucho sentido.

El código a continuación imprimirá la información de manera correcta, que tenga sentido y sin errores:
"""

# Commented out IPython magic to ensure Python compatibility.
# %%javascript
# let numeroUn = 1
# let stringUn = '1'
# let numeroTreinta = 30
# let stringTreinta = '30'
# let numeroDiez = 10
# let stringDiez = '10'
# 
# const nombreUsuario = prompt("Escribe tu nombre:");
# const edadUsuario = prompt ("¿Cuántos años tienes?") ;
# 
# if (numeroUn == stringUn) {
#   alert(`${nombreUsuario}: Las variables numeroUn y stringUn tienen el mismo valor, pero tipos diferentes`);
# } else {
#   alert(`${nombreUsuario} : Las variables numeroUn y stringUn no tienen el mismo valor`)
# }
# 
# if (numeroTreinta == stringTreinta) {
#   alert(`${nombreUsuario} : Las variables numeroTreinta y stringTreinta tienen el mismo valor y el mismo tipo`)
# } else {
#   alert('Las variables numeroTreinta y stringTreinta no tienen el mismo tipo')
# }
# 
# if (numeroDiez == stringDiez) {
#   alert('Las variables numeroDiez y stringDiez tienen el mismo valor, pero tipos diferentes')
# } else {
#   alert('Las variables numeroDiez y stringDiez no tienen el mismo valor')
# }
# 
# if (edadUsuario >= 18 ){
#   alert('Eres mayor de edad')
# } else {
#   alert('Aun eres menor de edad')
# }