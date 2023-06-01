import './tabela.css'

export default function TabelaComponente() {
   return (
      <div className="table">
         <table>
            <thead>
               <td>Livro</td>
               <td>Autor</td>
               <td>Ano</td>
            </thead>
            <tr>
               <th>O Homem que Ouve Cavalos</th>
               <th>Monty Roberts</th>
               <th>1996</th>
            </tr>
            <tr>
               <th>Violência Não é a Resposta</th>
               <th>Monty Roberts</th>
               <th>2002</th>
            </tr>
         </table>
      </div>
   )
}