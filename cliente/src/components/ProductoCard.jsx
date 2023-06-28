import React, { useState, useEffect } from 'react';
import { getDollar } from '../api/dolar.api';
import { format } from 'date-fns';

export function Dolar({ onDolarValue }) {
  const [dolar, setDolar] = useState(null);

  useEffect(() => {
    const obtenerDolar = async () => {
      try {
        const response = await getDollar();
        const data = response.data.Dolares;

        // Obtener el último día hábil antes de la fecha actual (excluyendo los fines de semana)
        const fechaActual = new Date();
        let fechaCercana = new Date(fechaActual);

        while (fechaCercana.getDay() === 0 || fechaCercana.getDay() === 6) {
          fechaCercana.setDate(fechaCercana.getDate() - 1);
        }

        // Buscar el valor del dólar para el último día hábil
        const fechaString = fechaCercana.toISOString().split('T')[0];
        const dolarValue = data.find(item => item.Fecha === fechaString)?.Valor;

        const formattedDolarValue = dolarValue.toString().replace(',', '.');

        const dolarValueFinal = parseFloat(formattedDolarValue);

        console.log(fechaCercana);

        setDolar({ valor: dolarValueFinal, fecha: fechaString });
        onDolarValue(dolarValueFinal, fechaString);
      } catch (error) {
        console.error(error);
      }
    };

    const cachedDolar = localStorage.getItem('dolarValue');
    if (cachedDolar) {
      const { valor, fecha } = JSON.parse(cachedDolar);
      setDolar({ valor, fecha });
      onDolarValue(valor, fecha);
    } else {
      obtenerDolar();
    }
  }, []);

  useEffect(() => {
    if (dolar) {
      localStorage.setItem('dolarValue', JSON.stringify(dolar));
    }
  }, [dolar]);

  return null;
}

export function ProductoCard({ product }) {
  const [dolarValue, setDolarValue] = useState(null);
  const [fechaDolar, setFechaDolar] = useState(null);

  const handleDolarValue = (valor, fecha) => {
    setDolarValue(valor);
    setFechaDolar(fecha);
  };

  return (
    <div>
      <Dolar onDolarValue={handleDolarValue} />
      <h5>{product.nombre}</h5>
      <p>{product.descripcion}</p>
      <p>CLP {product.precio}</p>
      {dolarValue && (
        <>
          <h6>USD {(product.precio / dolarValue).toFixed(2)}</h6>
          <h6>Valor Dolar al {format(new Date(fechaDolar), 'dd-MM-yyyy')}: ${dolarValue}</h6>
        </>
      )}
    </div>
  );
}
