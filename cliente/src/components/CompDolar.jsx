import React, { useState, useEffect } from 'react';
import axios from 'axios';

export function CompDolar(){
  const CompDolar = () => {
    const [dolar, setDolar] = useState(null);

    useEffect(() => {
      const obtenerDolar = async () => {
        try {
          const response = await axios.get('/obtener-dolar/');
          const mensaje = response.data.mensaje;
          console.log(mensaje); // Verifica que se hayan almacenado los datos en caché en Django

          // Obtén la fecha más cercana anterior a la actual
          const fechaActual = new Date();
          fechaActual.setHours(0, 0, 0, 0);
          let fechaCercana = new Date(fechaActual);
          fechaCercana.setDate(fechaCercana.getDate() - 1);

          // Consulta el valor del dólar para la fecha cercana
          let valorDolar = null;
          while (!valorDolar) {
            const fechaString = fechaCercana.toISOString().split('T')[0];
            valorDolar = response.data[`dolar_${fechaString}`];
            fechaCercana.setDate(fechaCercana.getDate() - 1);
          }

          setDolar(valorDolar);
        } catch (error) {
          console.error(error);
        }
      };

      obtenerDolar();
    }, []);

    return (
      <div>
        {dolar ? `Valor del dólar: $${dolar.toFixed(2)}` : 'Cargando...'}
      </div>
    );
  };
  }
