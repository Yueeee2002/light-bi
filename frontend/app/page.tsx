"use client";

import { Card, Descriptions, Space, Tag, Typography } from "antd";

const { Title, Paragraph, Text } = Typography;

/** 脚手架占位页：不含登录或业务功能。 */
export default function HomePage() {
  return (
    <main className="scaffold-page">
      <Card>
        <Space direction="vertical" size="large" style={{ width: "100%" }}>
          <div>
            <Title level={2} style={{ marginBottom: 8 }}>
              Light-BI 轻量自助 BI 平台
            </Title>
            <Paragraph type="secondary" style={{ marginBottom: 0 }}>
              阶段 1 脚手架已就绪：前后端框架、ORM 模型、种子账号与统一返回体。业务接口与页面将按阶段迭代。
            </Paragraph>
          </div>

          <Space wrap>
            <Tag color="blue">Next.js 14 App Router</Tag>
            <Tag color="geekblue">Ant Design v5</Tag>
            <Tag color="cyan">Recharts</Tag>
            <Tag>react-grid-layout</Tag>
            <Tag>Zustand</Tag>
            <Tag color="green">FastAPI</Tag>
            <Tag color="green">SQLAlchemy + SQLite</Tag>
          </Space>

          <Descriptions title="内置测试账号（后续登录阶段使用）" bordered size="small" column={1}>
            <Descriptions.Item label="admin">admin / 123456（管理员）</Descriptions.Item>
            <Descriptions.Item label="analyst">analyst / 123456（分析师）</Descriptions.Item>
            <Descriptions.Item label="viewer">viewer / 123456（查看者）</Descriptions.Item>
          </Descriptions>

          <Text type="secondary">后端探活：GET http://localhost:8000/health</Text>
        </Space>
      </Card>
    </main>
  );
}
