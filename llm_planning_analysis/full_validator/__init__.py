from model_parser.constants import *
from model_parser.parser_new import parse_model
from model_parser.writer_new import ModelWriter
from Executor import Executor

def get_all_errors(domain_file, problem_file, plan_file):
    ground = False # Keep this as the default
    executor = Executor(domain_file, problem_file, ground=ground)
    open_conditions = []
    with open(plan_file, 'r') as f:
        plan = f.readlines()
        f.close()
    plan = [line.strip() for line in plan]
    curr_state = executor.init_state
    for action in plan:
        action = action.replace('(', '').replace(')', '').replace(" ", "_")
        if executor.is_action_list_upper():
            action = action.upper()
        act_open_conditions = set()
        preconds, add_effects, del_effects = executor.ground_strips_action(action)
        # Find the preconds that are not satisfied
        act_open_conditions = set([precond for precond in preconds if precond not in curr_state])
        # Add the add effects to the current state
        curr_state = curr_state.union(add_effects)
        # Remove the delete effects from the current state
        curr_state = curr_state.difference(del_effects)
        open_conditions.append(list(act_open_conditions))
    
    unsatisfied_goal = executor.goal_state.difference(curr_state)

    precons_unsatisfied = any(len(open_conds) > 0 for open_conds in open_conditions)
    goal_unsatisfied = len(unsatisfied_goal) > 0

    feedback_dict = {
        'validation_info': 
            {
                'is_valid_plan': not (precons_unsatisfied or goal_unsatisfied),
            },
        'unmet_info': 
            {
                'unmet_precond': list(zip(plan, open_conditions)) if precons_unsatisfied else {} , 
                'unmet_goal': list(unsatisfied_goal) if goal_unsatisfied else []
             }
    }
    
    """
    Example:
    {
        'validation_info': {'is_valid_plan': False}, 
        'unmet_info': {
            'unmet_precond': [
                ('(pick-up_b)', {'ontable_b'}), 
                ('(stack_b_d)', set()), 
                ('(pick-up_a)', set()), 
                ('(stack_a_b)', set()), 
                ('(pick-up_d)', {'clear_d'}), 
                ('(stack_d_a)', set())
                ], 
            'unmet_goal': set()
            }
    }
    """
    return feedback_dict
        


# def generate_message(executor, plan, open_conditions, unsatisfied_goal):
#     if not any(len(open_conds) > 0 for open_conds in open_conditions):
#         if len(unsatisfied_goal) > 0:
#             message = f'The above plan is invalid.'
#             if len(unsatisfied_goal) > 1:
#                 f'These are the unmet goal conditions: {unsatisfied_goal}'
#         else:
#             return 'The above plan is valid.'
#     for act, open_conds in zip(plan, open_conditions):
#         if len(open_conds) > 0:
#             return f'Action {act} has open conditions {open_conds}'
                




if __name__=="__main__":
    domain = 'blocksworld'
    problem = 1
    domain_file = f'instances/{domain}/generated_domain.pddl'
    problem_file = f'instances/{domain}/generated_basic/instance-{problem}.pddl'
    plan_file = f'llm_sas_plan'
    get_all_errors(domain_file, problem_file, plan_file)