import React from "react";
import { Routes, Route } from "react-router-dom";
import Login from "../auth/Login";
import ProtectedRoute from "../auth/ProtectedRoute";
import DashboardLayout from "../components/layout/DashboardLayout";

import DashboardHome from "../modules/academics/ClassList"; // example default page

const AppRouter = () => {
  return (
    <Routes>
      <Route path="/" element={<Login />} />
      <Route
        path="/dashboard/*"
        element={
          <ProtectedRoute>
            <DashboardLayout>
              <DashboardHome />
            </DashboardLayout>
          </ProtectedRoute>
        }
      />
    </Routes>
  );
};

export default AppRouter;