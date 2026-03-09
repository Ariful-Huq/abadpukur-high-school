import { useState } from "react";
import { NavLink } from "react-router-dom";
import {
  LayoutDashboard,
  GraduationCap,
  Users,
  UserCog,
  CalendarCheck,
  CreditCard,
  ChevronLeft,
  ChevronRight,
} from "lucide-react";

export default function Sidebar() {
  const [collapsed, setCollapsed] = useState(false);

  const menu = [
    { name: "Dashboard", icon: LayoutDashboard, path: "/dashboard" },
    { name: "Academics", icon: GraduationCap, path: "/academics/classes" },
    { name: "Students", icon: Users, path: "/students" },
    { name: "Teachers", icon: UserCog, path: "/teachers" },
    { name: "Attendance", icon: CalendarCheck, path: "/attendance" },
    { name: "Fees", icon: CreditCard, path: "/fees" },
  ];

  return (
    <div
      className={`h-screen bg-slate-900 text-white flex flex-col transition-all duration-300 ${
        collapsed ? "w-20" : "w-64"
      }`}
    >
      {/* Top */}
      <div className="flex items-center justify-between p-4 border-b border-slate-700">
        {!collapsed && (
          <span className="text-lg font-semibold">School ERP</span>
        )}

        <button
          onClick={() => setCollapsed(!collapsed)}
          className="p-1 rounded hover:bg-slate-700"
        >
          {collapsed ? <ChevronRight size={18} /> : <ChevronLeft size={18} />}
        </button>
      </div>

      {/* Menu */}
      <nav className="flex-1 p-2 space-y-1">
        {menu.map((item) => {
          const Icon = item.icon;

          return (
            <NavLink
              key={item.name}
              to={item.path}
              className={({ isActive }) =>
                `flex items-center gap-3 p-2 rounded-md text-sm hover:bg-slate-700 transition ${
                  isActive ? "bg-slate-700" : ""
                }`
              }
            >
              <Icon size={20} />

              {!collapsed && <span>{item.name}</span>}
            </NavLink>
          );
        })}
      </nav>
    </div>
  );
}