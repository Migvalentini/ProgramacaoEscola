import React from 'react';
import ReactDOM from 'react-dom/client';
import reportWebVitals from './reportWebVitals';
import App from './componentes/App';
//import Oi from './componentes/oi';
import TabelaComponente from './componentes/tabela/tabela';

const root = ReactDOM.createRoot(
  document.getElementById('root') as HTMLElement
);
root.render(
  <React.StrictMode>
    <App />
    <TabelaComponente/>
  </React.StrictMode>
);

reportWebVitals();