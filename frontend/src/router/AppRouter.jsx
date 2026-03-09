import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import DashboardLayout from "../components/layout/DashboardLayout";

function DashboardHome() {
  return <div className="text-2xl">Dashboard Home</div>;
}

export default function AppRouter() {
  return (
    <BrowserRouter>
      <Routes>

        {/* redirect root */}
        <Route path="/" element={<Navigate to="/dashboard" replace />} />

        {/* dashboard */}
        <Route path="/dashboard" element={<DashboardLayout />}>
          <Route index element={<DashboardHome />} />
        </Route>

      </Routes>
    </BrowserRouter>
  );
}