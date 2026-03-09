import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";

import DashboardLayout from "../components/layout/DashboardLayout";

import Classes from "../modules/academics/pages/Classes";
import Sections from "../modules/academics/pages/Sections";
import Subjects from "../modules/academics/pages/Subjects";
import Routine from "../modules/academics/pages/Routine";

import Students from "../modules/students/pages/Students";
import Teachers from "../modules/teachers/pages/Teachers";
import Attendance from "../modules/attendance/pages/Attendance";
import Fees from "../modules/fees/pages/Fees";

function DashboardHome() {
  return <div className="text-2xl">Dashboard Home</div>;
}

export default function AppRouter() {
  return (
    <BrowserRouter>
      <Routes>

        <Route path="/" element={<Navigate to="/dashboard" replace />} />

        <Route path="/dashboard" element={<DashboardLayout />}>
          <Route index element={<DashboardHome />} />

          {/* Academics */}
          <Route path="academics/classes" element={<Classes />} />
          <Route path="academics/sections" element={<Sections />} />
          <Route path="academics/subjects" element={<Subjects />} />
          <Route path="academics/routine" element={<Routine />} />

          {/* Other modules */}
          <Route path="students" element={<Students />} />
          <Route path="teachers" element={<Teachers />} />
          <Route path="attendance" element={<Attendance />} />
          <Route path="fees" element={<Fees />} />

        </Route>

      </Routes>
    </BrowserRouter>
  );
}