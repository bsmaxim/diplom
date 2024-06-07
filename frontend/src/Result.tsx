interface ResultProps {
  text: string;
}

export const Result = (props: ResultProps) => {
  const { text } = props;

  return (
    <div className="content-center">
      <h2 className="font-extrabold text-3xl">Результат: </h2>
      <div className="flex justify-center mt-4">
        <p className="prose lg:prose-xl">{text}</p>
      </div>
    </div>
  );
};
