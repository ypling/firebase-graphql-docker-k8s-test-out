# Nginx

k8s_yaml(['nginx/k8s/nginx.yaml', 'nginx/k8s/nginx-config.yaml'])
k8s_resource(objects=['nginx-config:ConfigMap:default'], new_name='nginx-config')

# UI
# check if UI repo has been checked out
USE_UI = os.path.exists('./graphql-api/k8s')
if USE_UI:
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

k8s_yaml('ui/k8s/ui.yaml')
k8s_resource('ui-deployment', new_name='ui')

# GraphQL
# check if graphql repo checked out
USE_GRAPHQL = os.path.exists('./graphql-api/k8s')
if USE_GRAPHQL:
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
    k8s_yaml('graphql-api/k8s/graphql.yaml')
    k8s_resource('graphql-deployment', new_name='graphql')

# PostgreSQL DB
k8s_yaml('postgresql-db/k8s/postgresql.yaml')
k8s_resource('postgresql-deployment', new_name='postgresql-db')