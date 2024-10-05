"use client";

import CustomButton from "@/components/CustomButton";
import { useAccount } from "wagmi";

export default function Home() {
  const { isConnected } = useAccount();

  return (
    <main className="min-h-screen px-8 py-0 pb-12 flex-1 flex flex-col items-center">
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4 max-w-4xl w-full">
        <div className="grid bg-white border border-gray-200 rounded-lg overflow-hidden shadow-sm">
          <h3 className="text-sm font-semibold bg-gray-100 p-2">Connect wallet</h3>
          <div className="flex justify-center items-center p-4">
            <w3m-button size="md" />
          </div>
        </div>

      </div>
    </main>
  );
}
