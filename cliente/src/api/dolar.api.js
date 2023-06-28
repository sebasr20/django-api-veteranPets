import axios from "axios";

export const getDollar = () => {
  const currentDate = new Date();
  const year = currentDate.getFullYear();
  // El mes se devuelve en base 0, por lo que es necesario sumar 1 al valor obtenido
  const month = currentDate.getMonth() + 1;

  const url =
    "https://api.sbif.cl/api-sbifv3/recursos_api/dolar/2023/06?apikey=eba350313ffa85eb44616c08949737ca082d6fc3&formato=JSON";
  return axios.get(url);
};
