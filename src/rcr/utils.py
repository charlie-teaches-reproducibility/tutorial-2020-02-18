def print_where_we_are():
    print(f"We're in {__name__} in {__file__}")
    print('im trapped in a universe factory')
    print('still trapped... in the closet')
    print('still trapped... in the closet... its safe in here with tom cruise')


def get_my_prisoner_number():
    return 24601


def get_who_am_i():
    return "I'm Jean Val Jean"


def do_my_super_stuff(graph, df) -> 'pd.DataFrame':
    raise NotImplementedError


def do_my_super_path_stuff(graph_path: str, df_path: str, output_path: str) -> None:
    graph = get_graph(graph_path)
    df = pd.read_csv(df_path)
    results_df = do_my_super_stuff(graph, df)
    results_df.to_csv(output_path)


if __name__ == '__main__':
    print('this is being run as a script')
    print_where_we_are()
