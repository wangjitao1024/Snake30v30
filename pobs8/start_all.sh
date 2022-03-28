nohup python -u actor.py --num_replicas=20 --data_port=5000 --param_port=5001 > ./log/actor.log &
nohup python -u learner.py --pool_size=16384 --batch_size=16384 --data_port=5000 --param_port=5001 > ./log/learner.log &

# python actor.py --num_replicas=10 --data_port=5000 --param_port=5001
# python learner.py --pool_size=16384 --batch_size=16384 --data_port=5000 --param_port=5001
