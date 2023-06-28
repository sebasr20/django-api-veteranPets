import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom"
import { Productos } from "./pages/Productos/Productos"
import { Destacados } from "./pages/Destacados/Destacados"
import { Monedas } from "./pages/Monedas/Monedas"

function App() {
  return (
    <BrowserRouter>
      <Routes>
        {/* <Route path="/" element={Navigate to="/productos"} Por si necesito redireccionar a una ruta*/}
        <Route path="/" element={<Destacados/>} />
        <Route path="/productos" element={<Productos/>} />
        <Route path="/monedas" element={<Monedas />} />
      </Routes>
    </BrowserRouter>
  )
}

export default App