docker_build(
    'firebase-graphql-docker-k8s',
    context='.',
    dockerfile='./Dockerfile',
    build_args={'node_env': 'development'},
    entrypoint='npx nodemon index.js',
    only=['index.js', 'package.json', 'package-lock.json'],
    live_update=[
        sync('index.js', '/usr/app/index.js'),
    ]
)

k8s_yaml('k8s/graphql.yaml')
k8s_resource('graphql-deployment')