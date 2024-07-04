docker_build(
    'firebase-graphql-docker-k8s',
    context='graphql-api',
    dockerfile='./graphql-api/Dockerfile',
    build_args={'node_env': 'development'},
    entrypoint='npx nodemon index.js',
    only=['index.js', 'package.json', 'package-lock.json', 'middlewares', 'secrets'],
    live_update=[
        sync('graphql-api/index.js', '/usr/app/index.js'),
    ]
)

docker_build(
    'architect-design-poc-ui',
    context='ui',
    dockerfile='./ui/Dockerfile',
    build_args={'node_env': 'development'},
    entrypoint='npm run dev',
    only=['src', 'webpack.config.js', 'package.json', 'package-lock.json'],
    live_update=[
        sync('ui/src', '/usr/app/src'),
    ]
)

k8s_yaml('nginx/k8s/nginx.yaml')
k8s_resource('nginx-deployment')

k8s_yaml('graphql-api/k8s/graphql.yaml')
k8s_resource('graphql-deployment')

k8s_yaml('ui/k8s/ui.yaml')
k8s_resource('ui-deployment')

k8s_yaml('postgresql-db/k8s/postgresql.yaml')
k8s_resource('postgresql-deployment')