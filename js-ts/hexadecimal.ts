function inverterString(str: string): string {
   let invertedString = '';
   for (let i = str.length - 1; i >= 0; i--) {
     invertedString += str[i];
   }
   return invertedString;
 }
 
 function converter(num: number): string {
   let resto: number = 0;
   let hexadecimal: string = '';
   let stringResto: string = '';
 
   while (num >= 16) {
     resto = num % 16;
     num = Math.floor(num / 16);
     stringResto = resto.toString();
 
     if (stringResto === '10') {
       hexadecimal += 'A';
     } else if (stringResto === '11') {
       hexadecimal += 'B';
     } else if (stringResto === '12') {
       hexadecimal += 'C';
     } else if (stringResto === '13') {
       hexadecimal += 'D';
     } else if (stringResto === '14') {
       hexadecimal += 'E';
     } else if (stringResto === '15') {
       hexadecimal += 'F';
     } else {
       hexadecimal += stringResto;
     }
   }
 
   stringResto = num.toString();
   hexadecimal += stringResto;
   hexadecimal = inverterString(hexadecimal);
   return hexadecimal;
 }
 
 console.log(converter(438));