(define (problem BW-generalization-4)
(:domain blocksworld-4ops)(:objects e c h l k d)
(:init 
(handempty)
(ontable e)
(ontable c)
(ontable h)
(ontable l)
(ontable k)
(ontable d)
(clear e)
(clear c)
(clear h)
(clear l)
(clear k)
(clear d)
)
(:goal
(and
(on e c)
(on c h)
(on h l)
(on l k)
(on k d)
)))