import type { Metadata } from "next";

import AntdProvider from "@/components/providers/AntdProvider";

import "./globals.css";

export const metadata: Metadata = {
  title: "Light-BI 轻量自助 BI 平台",
  description: "面向企业内部分析师的轻量化自助 BI 可视化平台（MVP）",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="zh-CN">
      <body>
        <AntdProvider>{children}</AntdProvider>
      </body>
    </html>
  );
}
