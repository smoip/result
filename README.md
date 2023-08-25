# Result

Cheap and cheerful monad-inspired result handling for Python.  
Provides a generic API for arbitrary actions to simplify error handling and control flow.  
Enforces presence of `success` and `failure` on `Result` instances.  
Calls to `succeed` must supply a content object, which can then be safely accessed.  
Calls to `fail` must supply an error object, which can then be safely accessed.  

Types are not enforced for `content` or `error`, but it would be simple to subclass `Result` to enforce return types for different business use cases.

## Usage

Given a `MyServiceClass` that executes arbitrary business logic:
```
from result import Result

class MyServiceClass:
    @classmethod
    def execute(cls):
        ...
        # Business logic
        if happy_path:
            return Result.succeed(business_logic_outcome)
        else:
            return Result.fail(pertinent_error_info)
```

And a `MyOuterClass` that invokes the service class:
```
class MyOuterClass:
    @classmethod
    def execute_services(cls):
        r = MyServiceClass.execute()
        if r.success:
            print(f"success with content: {r.content}") # safely access `content`
        else:
            print(f"failed with error: {r.error}") # safely access `error`
```
