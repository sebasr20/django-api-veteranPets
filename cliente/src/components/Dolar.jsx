import { useEffect, useState } from "react";
import axios from 'axios';

export function Dolar() {
  const [dolares, setDolares] = useState([]);

  useEffect(() => {
    async function loadDolar() {
      try {
        const res = await axios.get('https://api.sbif.cl/api-sbifv3/recursos_api/dolar/2023/06  ?apikey=eba350313ffa85eb44616c08949737ca082d6fc3&formato=JSON');
        console.log(res.data);          
        setDolares(res.data.Dolares);
      } catch (error) {
        console.error(error);
      }
    }

    loadDolar();
  }, []);

  return (
    <>
      <h1>Valor Dolar de Junio</h1>
      <ul>
        {dolares.map((dolar, index) => (
          <li key={index}>{dolar.Fecha} - {dolar.Valor}</li>
        ))}
      </ul>
    </>
  );
}
