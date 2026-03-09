export default function Header() {
  return (
    <header className="h-16 bg-white border-b flex items-center justify-between px-6">
      <h1 className="text-xl font-semibold text-gray-700">
        Dashboard
      </h1>

      <div className="flex items-center gap-4">
        <span className="text-sm text-gray-600">
          Admin
        </span>

        <div className="w-8 h-8 rounded-full bg-gray-300" />
      </div>
    </header>
  );
}