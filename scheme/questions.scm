(define (caar x) (car (car x)))
(define (cadr x) (car (cdr x)))
(define (cdar x) (cdr (car x)))
(define (cddr x) (cdr (cdr x)))

; Some utility functions that you may find useful to implement.
(define (map proc items)
  (if (null? items) nil
    (cons (proc (car items)) (map proc (cdr items)))
  )
)

(define (cons-all first rests)
  (map (lambda (x) (cons first x)) rests)
)



(define (zip pairs)
  (define (left pairs)
    (cond
      ((null? pairs) pairs)
      (else (cons (caar pairs) (left (cdr pairs))))
    )
  )
  (define (right pairs)
    (cond
      ((null? pairs) pairs)
      (else (cons (car (cdr (car pairs))) (right (cdr pairs))))
    )
  )
  (cons (left pairs) (cons (right pairs) nil))
)

;; Problem 17
(define (m-builder index lst)
  (if (null? lst) '()
    (cons (list index (car lst)) (m-builder (+ 1 index) (cdr lst)))
  )
)

(define (enumerate s)
  ; BEGIN PROBLEM 17
  (m-builder 0 s)
)
  ; END PROBLEM 17

;; Problem 18
;; List all ways to make change for TOTAL with DENOMS
(define (list-change total denoms)
  (cond
    ((null? denoms) '())
    ((< (- total (car denoms)) 0) (list-change total (cdr denoms)))
    ((= (- total (car denoms)) 0)
      (append (cons (cons (car denoms) nil) nil) (list-change total (cdr denoms)))
    )

    (else
      (begin
        (define has (cons-all (car denoms) (list-change (- total (car denoms)) denoms)))
        (define lacks (list-change total (cdr denoms)))
        (append has lacks)
      )
    )
  )
)
  ; END PROBLEM 18

;; Problem 19
;; Returns a function that checks if an expression is the special form FORM
(define (check-special form)
  (lambda (expr) (equal? form (car expr))))

(define lambda? (check-special 'lambda))
(define define? (check-special 'define))
(define quoted? (check-special 'quote))
(define let?    (check-special 'let))

;; Converts all let special forms in EXPR into equivalent forms using lambda
(define (let-to-lambda expr)
  (cond
         ((atom? expr) ; todo this is a primitive type
         ; BEGIN PROBLEM 19
         expr
         ; END PROBLEM 19
         )
         ((quoted? expr)
         ; BEGIN PROBLEM 19
         expr
         ; END PROBLEM 19
         )
         ((or (lambda? expr)
             (define? expr))
         (let ((form   (car expr))
               (params (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM 19
           (append (list form) (list (map let-to-lambda params)) (map let-to-lambda body))
           ; END PROBLEM 19
           ))
        ((let? expr)
         (let ((values (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM 19
           (append (list
             (append (list 'lambda (map let-to-lambda (car (zip values)))) (map let-to-lambda body)))
              (map let-to-lambda (cadr (zip values))))
           ; END PROBLEM 19
           ))
        (else
         ; BEGIN PROBLEM 19
         (map let-to-lambda expr)
         ; END PROBLEM 19
         )))
