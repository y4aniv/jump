import "@/styles/globals.css";
import type { Metadata } from "next";

const metadata: Metadata = {
  title: "Jump - Faites le saut vers la simplicité",
  description:
    "Solution de click and collect pour les commerces de proximité [NSI]",
};

const RootLayout: React.FC<{ children: React.ReactNode }> = ({
  children,
}): React.ReactElement => {
  return (
    <html lang="fr">
      <body>{children}</body>
    </html>
  );
};

export { metadata };
export default RootLayout;
