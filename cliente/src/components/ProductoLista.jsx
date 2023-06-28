import { useEffect, useState } from "react"
import { getAllProducts } from "../api/productos.api";
import { ProductoCard } from "./ProductoCard";

export function ProductoLista() {

    const [products, setProducts] = useState([]);

    useEffect(() => {
        async function loadProducts(){
            const res = await getAllProducts();

            console.log(res.data);
            setProducts(res.data);
        }
        loadProducts();
    }, []);

  return (
    <>
      <h1>Lista Productos</h1>
      {products.map(product => (
        <ProductoCard key={product.id} product={product} />        
      ))}
    </>
  )
}