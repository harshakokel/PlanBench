(define (problem BW-generalization-4)
(:domain blocksworld-4ops)(:objects j e h d f i a)
(:init 
(handempty)
(ontable j)
(ontable e)
(ontable h)
(ontable d)
(ontable f)
(ontable i)
(ontable a)
(clear j)
(clear e)
(clear h)
(clear d)
(clear f)
(clear i)
(clear a)
)
(:goal
(and
(on j e)
(on e h)
(on h d)
(on d f)
(on f i)
(on i a)
)))