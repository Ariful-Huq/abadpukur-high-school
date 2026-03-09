import React from "react";
import { Link, useLocation } from "react-router-dom";

const Sidebar = () => {
  const location = useLocation();

  const menu = [
    { name: "Dashboard", path: "/dashboard" },
    { name: "Academics", path: "/dashboard/academics" },
    { name: "Students", path: "/dashboard/students" },
    { name: "Teachers", path: "/dashboard/teachers" },
    { name: "Attendance", path: "/dashboard/attendance" },
    { name: "Fees", path: "/dashboard/fees" },
  ];

  return (
    <div className="w-64 bg-gray-900 text-white min-h-screen p-5">
      <h2 className="text-xl font-bold mb-6">School Admin</h2>
      <nav>
        {menu.map((item) => (
          <Link
            key={item.path}
            to={item.path}
            className={`block p-3 mb-2 rounded ${
              location.pathname.startsWith(item.path) ? "bg-gray-700" : ""
            }`}
          >
            {item.name}
          </Link>
        ))}
      </nav>
    </div>
  );
};

export default Sidebar;