import React from 'react';
import '../App.css';
import daniel from '../img/daniel.jpg'
import alana2 from '../img/alana2.jpg'
import diego from '../img/diego.jpg'

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>TCC - Trabalho de Conclusão de Curso</h1>
        <div className='imagens'>
          <img src={daniel} alt="Erro" className='img'/>
          <img src={alana2} alt="Erro" className='img' id='alana'/>
          <img src={diego} alt="Erro" className='img' id='diego'/>
        </div>
      </header>
    </div>
  );
}

export default App;
